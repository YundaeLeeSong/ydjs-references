import pygame
import math
import random
import time



class Enemy:
    def __init__(self, surface_width, surface_height, size_x, size_y, back_x, back_y):
        self.phase = 1
        self.phase_counter = 0

        self.hp = 130
        self.exp = 100

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

    def catch(self, player):
        t = []
        t.append(self.enemy_rect_object)
        if self.enemy_rect_object.colliderect(player.player_rect_object):
            player.damaged_by(self.enemy_rect_object, t, self.body_damage)


class Illene:
    def __init__(self, surface_width, surface_height, size_x, size_y, back_x, back_y):
        self.phase = 1
        self.phase_counter = 0

        self.hp = 80
        self.exp = 200

        self.enemy_width = 33
        self.enemy_height = 33

        self.screen_width = surface_width
        self.screen_height = surface_height
        self.size_x = size_x
        self.size_y = size_y

        self.move_x_pos = random.randrange(-self.screen_width * (self.size_x - 1), self.screen_width - self.enemy_width)
        self.move_y_pos = random.randrange(-self.screen_height * (self.size_y - 1),
                                           self.screen_height - self.enemy_height)
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y
        self.move_x_dir = 0  # for skill direction
        self.move_y_dir = 2  # for skill direction
        self.counter = 0
        self.pattern = random.randrange(100)

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)

    def make_movement1(self, back_x, back_y):
        dx = 0
        dy = 1

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
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







class Killer:
    def __init__(self, surface_width, surface_height, size_x, size_y, back_x, back_y):
        self.phase = 1
        self.phase_counter = 0

        self.hp = 500
        self.exp = 400

        self.body_damage = 5

        self.enemy_width = 33
        self.enemy_height = 33

        self.screen_width = surface_width
        self.screen_height = surface_height
        self.size_x = size_x
        self.size_y = size_y

        self.move_x_pos = random.randrange(-self.screen_width * (self.size_x - 1),
                                           self.screen_width - self.enemy_width)
        self.move_y_pos = random.randrange(-self.screen_height * (self.size_y - 1),
                                           self.screen_height - self.enemy_height)
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y
        self.move_x_dir = 0  # for skill direction
        self.move_y_dir = 2  # for skill direction
        self.counter = 0
        self.pattern = random.randrange(100)

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)

        ## Shadow made
        self.shadow_x = random.randrange(-self.screen_width * (self.size_x - 1),
                                         self.screen_width - self.enemy_width)
        self.shadow_y = random.randrange(-self.screen_height * (self.size_y - 1),
                                           self.screen_height - self.enemy_height)
        self.shadow_w = 200
        self.shadow_h = 200

        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

    def make_movement1(self, back_x, back_y):
        dx = 0
        dy = 1

        ## set direction
        self.move_x_dir, self.move_y_dir = dx, dy

        ## movement make
        self.move_x_pos += dx
        self.move_y_pos += dy
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)
        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)
        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)

        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)

        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

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
        if not (-self.screen_width * (
                self.size_x - 1) < self.move_x_pos and self.move_x_pos < self.screen_width - self.enemy_width
                and -self.screen_height * (
                        self.size_y - 1) < self.move_y_pos and self.move_y_pos < self.screen_height - self.enemy_height):
            self.move_x_pos -= dx
            self.move_y_pos -= dy

        ## generate actual location on screen
        self.move_x_pos_onscreen = self.move_x_pos + back_x
        self.move_y_pos_onscreen = self.move_y_pos + back_y

        self.enemy_rect_object = pygame.Rect(int(self.move_x_pos_onscreen),
                                             int(self.move_y_pos_onscreen),
                                             self.enemy_width,
                                             self.enemy_height)

        ## Shadow onscreen
        self.shadow_x_onscreen = self.shadow_x + back_x
        self.shadow_y_onscreen = self.shadow_y + back_y

        self.shadow_rect_object = pygame.Rect(int(self.shadow_x_onscreen), int(self.shadow_y_onscreen),
                                              self.shadow_w, self.shadow_h)

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

    def catch(self, player):
        t = []
        t.append(self.enemy_rect_object)
        if self.enemy_rect_object.colliderect(player.player_rect_object):
            player.damaged_by(self.enemy_rect_object, t, self.body_damage)

    def get_shadow(self):
        return self.shadow_rect_object