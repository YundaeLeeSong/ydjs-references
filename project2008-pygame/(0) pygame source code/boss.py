import pygame
import math
import random
import time



class Boss:
    def __init__(self, surface_width, surface_height, size_x, size_y, back_x, back_y):
        self.phase = 1
        self.phase_counter = 0
        self.muda_side = 200


        self.hp = 5000
        self.exp = 2000

        self.the_world_counter = -1

        self.muda_counter = 5500
        self.muda_damage = 1

        self.body_damage = 1

        self.enemy_width = 33
        self.enemy_height = 33

        self.screen_width = surface_width
        self.screen_height = surface_height
        self.size_x = size_x
        self.size_y = size_y


        self.move_x_pos = random.randrange(-self.screen_width * (self.size_x - 1), self.screen_width - self.enemy_width)
        self.move_y_pos = random.randrange(-self.screen_height * (self.size_y - 1), self.screen_height - self.enemy_height)
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y
        self.move_x_dir = 0 # for skill direction
        self.move_y_dir = 2 # for skill direction
        self.counter = 0
        self.pattern = random.randrange(100)
        

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)


    def make_movement_to_player(self, back_x, back_y, player_rect):

        if self.can_muda(player_rect):
            dx = 0.4 * (player_rect.x - self.move_x_pos_onscreen) / math.sqrt((player_rect.x - self.move_x_pos_onscreen)**2 + (player_rect.y - self.move_y_pos_onscreen)**2)
            dy = 0.4 * (player_rect.y - self.move_y_pos_onscreen) / math.sqrt((player_rect.x - self.move_x_pos_onscreen)**2 + (player_rect.y - self.move_y_pos_onscreen)**2)
        else:
            dx = 1 * (player_rect.x - self.move_x_pos_onscreen) / math.sqrt(
                (player_rect.x - self.move_x_pos_onscreen) ** 2 + (player_rect.y - self.move_y_pos_onscreen) ** 2)
            dy = 1 * (player_rect.y - self.move_y_pos_onscreen) / math.sqrt(
                (player_rect.x - self.move_x_pos_onscreen) ** 2 + (player_rect.y - self.move_y_pos_onscreen) ** 2)


        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1

    def make_movement1(self, back_x, back_y):
        dx = 0
        dy = 1

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1



    def make_movement2(self, back_x, back_y):
        dx = 1
        dy = 0

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1

    def make_movement3(self, back_x, back_y):
        dx = 0
        dy = -1

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1


    def make_movement4(self, back_x, back_y):
        dx = -1
        dy = 0

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1

    def make_movement5(self, back_x, back_y):
        dx = 0
        dy = 0

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                           int(self.move_y_pos_onscreen),
                                           self.enemy_width,
                                           self.enemy_height)
        self.counter += 1
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1

    def get_counter(self):
        return self.counter

    def reset_pattern(self):
        self.counter = 0
        self.pattern = random.randrange(100)

    def get_pattern(self):
        return self.pattern



    def get_enemy_rect(self):
        return self.enemy_rect_object








    # Logic - enemy
    def is_death(self):
        answer = False
        if self.hp <= 0:
            answer = True
        return answer

    def damaged_by(self, player, rect_list, damge_amount):
        if self.enemy_rect_object.collidelist(rect_list) >= 0 and self.hp > 0:
            self.hp -= damge_amount
            if self.hp <= 0:
                player.increase_exp(self.exp)



    def is_use_THE_WORLD(self):
        use = False
        choice = random.randrange(10000)
        if choice == 777 or choice == 77 or choice == 7 or choice == 700 or choice == 770 or choice == 7700 or choice == 7777:
            self.the_world_counter = 0
            use = True
        return use

    def is_THE_WORLD(self):
        result = False
        if self.the_world_counter >= 0 and self.the_world_counter < 1000: # about 2sec
            self.the_world_counter += 1
            result = True
        else:
            self.the_world_counter = -1
            result = False
        return result




    def count_muda(self):
        self.muda_counter += 1
        if self.muda_counter < 3000:
            self.muda_counter += 1
        if self.muda_counter > 5500:
            self.muda_counter -= 1

    def can_muda(self, player_rect):
        use = False
        if math.sqrt((player_rect.x - self.move_x_pos_onscreen)**2 + (player_rect.y - self.move_y_pos_onscreen)**2) < 170:
            use = True
        return use

    def is_muda(self):
        result = False
        if self.muda_counter > 100:
            self.muda_counter -= 20
            result = True
        return result

    def muda_recharge(self):
        if random.randrange(0, 1000) == 2:
            self.muda_counter = 5500





    def get_skill_muda(self):
        self.muda_skill = pygame.Rect(int(self.enemy_rect_object.centerx - self.muda_side / 2 + self.move_x_dir * 100),
                                      int(self.enemy_rect_object.centery - self.muda_side / 2 + self.move_y_dir * 100),
                                      self.muda_side,
                                      self.muda_side),
        return self.muda_skill

    def get_muda_x(self):
        return int(self.enemy_rect_object.centerx - self.muda_side / 2 + self.move_x_dir * 100)

    def get_muda_y(self):
        return int(self.enemy_rect_object.centery - self.muda_side / 2 + self.move_y_dir * 100)

    def get_skill_muda_damage(self):
        return self.muda_damage

    def catch(self, player):
        t = []
        t.append(self.enemy_rect_object)
        if self.enemy_rect_object.colliderect(player.player_rect_object):
            player.damaged_by(self.enemy_rect_object, t, self.body_damage)




