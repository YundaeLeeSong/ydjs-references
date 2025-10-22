import pygame
import math
import random
import time




class Character:
    def __init__(self, surface_width, surface_height):
        self.level = 1
        self.hp = 1000
        self.maxHp = 1000
        self.exp = 0
        self.exp_required = 1000 # increase 20% at each level up

        self.mode_explain = False
        self.story_explain = False


        ###############################################
        self.seen_intro_tutorial = False
        self.seen_intro_random = False
        self.seen_intro_1 = False
        self.seen_intro_2 = False
        self.seen_intro_3 = False
        ###############################################

        self.skill2_notice = False
        self.skill3_notice = False
        self.skill4_notice = False

        self.screen_width = surface_width
        self.screen_height = surface_height
        self.move_straight = 2
        self.move_diagonal = self.move_straight / math.sqrt(2)

        self.player_width = 33
        self.player_height = 33
        self.player_range = 20
        self.skill_side = 10

        self.skill_a_delay = 0.2
        self.skill_s1_delay = 1.2
        self.skill_s2_delay = 0.5
        self.skill_d_delay = 1.8 / 5
        self.skill_f_delay = 1.2 / 6

        self.skill_1_damage = 24
        self.skill_2_damage = 80
        self.skill_3_damage = 100

        self.a_counter = 0
        self.a_image_couter = 1000
        self.phase = 1
        self.phase_counter = 0
        self.move_x_pos = self.screen_width / 2
        self.move_y_pos = self.screen_height / 2
        self.move_dx = 0
        self.move_dy = 0
        self.move_x_dir = 0
        self.move_y_dir = self.move_straight
        self.skill_a_use = False
        self.skill_s_use = False
        self.skill_d_use = False
        self.skill_f_use = False
        self.reload = False
        self.reload_counter = 0
        self.flagX = False
        self.temp_backX = 300000
        self.flagY = False
        self.temp_backY = 300000
        self.bullet = 6

        self.player_rect_object = pygame.Rect(int(self.move_x_pos),
                                           int(self.move_y_pos),
                                           self.player_width,
                                           self.player_height)

        self.skill_1_rect_object = self.get_skill_1(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_2_rect_object = self.get_skill_2(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_3_rect_object = self.get_skill_3(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)












    def get_player_rect(self):
        return self.player_rect_object

    def get_skill_1_rect(self):
        return self.skill_1_rect_object

    def get_skill_2_rect(self):
        return self.skill_2_rect_object

    def get_skill_3_rect(self):
        return self.skill_3_rect_object

    def get_skill_1_damage(self):
        return self.skill_1_damage

    def get_skill_2_damage(self):
        return self.skill_2_damage

    def get_skill_3_damage(self):
        return self.skill_3_damage





    def get_a_delay(self):
        return self.skill_a_delay

    def get_s1_delay(self):
        return self.skill_s1_delay

    def get_s2_delay(self):
        return self.skill_s2_delay

    def get_d_delay(self):
        return self.skill_d_delay

    def get_f_delay(self):
        return self.skill_f_delay


    def use_bullet(self):
        self.bullet -= 1
    def reload_bullet(self):
        self.bullet += 1

    def get_bullet(self):
        return self.bullet

    def can_reload(self):
        result = False
        if self.reload_counter >= 0 and self.reload_counter < 30:
            self.reload_counter += 1
            result = False
        else:
            self.reload_counter = 0
            result = True
        if not (0 <= self.bullet and self.bullet < 6):
            result = False
        return result



    def make_movement(self, keyboard_changeX, keyboard_changeY, backX, numX, backY, numY):
        if (self.temp_backX != backX):
            self.temp_backX = backX
        elif (self.temp_backX == backX and keyboard_changeX != 0 and (backX < 2 or backX > self.screen_width * (numX - 1) - 2)):
            self.flagX = True

        if (self.temp_backY != backY):
            self.temp_backY = backY
        elif (self.temp_backY == backY and keyboard_changeY != 0 and (backY < 2 or backY > self.screen_height * (numY - 1) - 2)):
            self.flagY = True

        self.move_dx, self.move_dy = self.keyinput_validation(keyboard_changeX, keyboard_changeY)
        self.move_x_dir, self.move_y_dir = self.get_direction(self.move_x_dir,
                                                         self.move_y_dir,
                                                         self.move_dx,
                                                         self.move_dy)

        tempX, tempY = self.set_location(self.move_x_pos,
                                         self.move_y_pos,
                                         self.move_dx,
                                         self.move_dy)

        self.move_x_pos, self.move_y_pos = self.screen_width / 2 - self.player_width / 2 + 2, \
                                           self.screen_height / 2 - self.player_height / 2 + 2
        self.back_dx, self.back_dy = (-self.move_dx, -self.move_dy)

        if self.flagX: ####
            self.move_x_pos = tempX
            self.back_dx = 0

        if (abs(int(self.move_x_pos) - (self.screen_width / 2 - self.player_width / 2)) < 2) and self.flagX: ####
            self.move_x_pos = self.screen_width / 2 - self.player_width / 2
            self.back_dx = -self.move_dx
            self.flagX = False

        if self.flagY: ####
            self.move_y_pos = tempY
            self.back_dy = 0

        if (abs(int(self.move_y_pos) - (self.screen_height / 2 - self.player_height / 2)) < 2) and self.flagY: ####
            self.move_y_pos = self.screen_height / 2 - self.player_height / 2
            self.back_dy = -self.move_dy
            self.flagY = False


        self.player_rect_object = pygame.Rect(int(self.move_x_pos),
                                              int(self.move_y_pos),
                                              self.player_width,
                                              self.player_height)
        self.skill_1_rect_object = self.get_skill_1(self.player_rect_object,
                                                    (self.move_dx, self.move_dy,
                                                     self.move_x_dir, self.move_y_dir),
                                                    self.player_range)
        self.skill_2_rect_object = self.get_skill_2(self.player_rect_object,
                                                    (self.move_dx, self.move_dy,
                                                     self.move_x_dir, self.move_y_dir),
                                                    self.player_range)
        self.skill_3_rect_object = self.get_skill_3(self.player_rect_object,
                                                    (self.move_dx, self.move_dy,
                                                     self.move_x_dir, self.move_y_dir),
                                                    self.player_range)
        self.phase_counter += 1
        if self.phase_counter > 20:
            self.phase_counter = 0
            self.phase += 1
            if self.phase == 4:
                self.phase = 1



    def set_location(self, x, y, dx, dy):
        x += dx
        y += dy
        if (x > self.screen_width - self.player_width or x < 0
            or
            y > self.screen_height - self.player_height or y < 0):
            x -= dx
            y -= dy
        return x, y

        


    def get_direction(self, x_direction, y_direction, dx, dy):
        if not (dx == 0 and dy == 0):
            a = dx
            b = dy
        else:
            a = x_direction
            b = y_direction
        return a, b

    def keyinput_validation(self, var_changeX, var_changeY):
        if abs(math.sqrt(var_changeX ** 2 + var_changeY ** 2) - self.move_straight) > 0.01:
            if var_changeX * var_changeY != 0:
                var_changeX = var_changeX / abs(var_changeX) * math.sqrt(2)
                var_changeY = var_changeY / abs(var_changeY) * math.sqrt(2)
            if var_changeX == 0 and var_changeY < 0:
                var_changeY = -self.move_straight
            if var_changeX == 0 and var_changeY > 0:
                var_changeY = self.move_straight
            if var_changeY == 0 and var_changeX < 0:
                var_changeX = -self.move_straight
            if var_changeY == 0 and var_changeX > 0:
                var_changeX = self.move_straight
        return var_changeX, var_changeY
    
    def get_skill_3(self, player_rect, direction_list, skill_len):
        list_of_rectangles = []
        x = player_rect.x
        y = player_rect.y
        w = player_rect.w
        h = player_rect.h
        if direction_list[2] == 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 12, y, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect3 = self.get_skill_1(pygame.Rect(x - 12, y, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect4 = self.get_skill_1(pygame.Rect(x + 24, y, w ,h), direction_list, skill_len, 20)
            rect5 = self.get_skill_1(pygame.Rect(x - 24, y, w ,h), direction_list, skill_len, 20)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
            for x in rect4:
                list_of_rectangles.append(x)
            for x in rect5:
                list_of_rectangles.append(x)
        elif direction_list[3] == 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x, y + 12, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect3 = self.get_skill_1(pygame.Rect(x, y - 12, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect4 = self.get_skill_1(pygame.Rect(x, y + 24, w ,h), direction_list, skill_len, 20)
            rect5 = self.get_skill_1(pygame.Rect(x, y - 24, w ,h), direction_list, skill_len, 20)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
            for x in rect4:
                list_of_rectangles.append(x)
            for x in rect5:
                list_of_rectangles.append(x)
        elif direction_list[2] * direction_list[3] > 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 8, y - 8, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect3 = self.get_skill_1(pygame.Rect(x - 8, y + 8, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect4 = self.get_skill_1(pygame.Rect(x + 16, y - 16, w ,h), direction_list, skill_len, 20)
            rect5 = self.get_skill_1(pygame.Rect(x - 16, y + 16, w ,h), direction_list, skill_len, 20)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
            for x in rect4:
                list_of_rectangles.append(x)
            for x in rect5:
                list_of_rectangles.append(x)
        elif direction_list[2] * direction_list[3] < 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 8, y + 8, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect3 = self.get_skill_1(pygame.Rect(x - 8, y - 8, w ,h), direction_list, int(skill_len * 1.2), 15)
            rect4 = self.get_skill_1(pygame.Rect(x + 16, y + 16, w ,h), direction_list, skill_len, 20)
            rect5 = self.get_skill_1(pygame.Rect(x - 16, y - 16, w ,h), direction_list, skill_len, 20)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
            for x in rect4:
                list_of_rectangles.append(x)
            for x in rect5:
                list_of_rectangles.append(x)
            
        return list_of_rectangles

    def get_skill_2(self, player_rect, direction_list, skill_len):
        list_of_rectangles = []
        x = player_rect.x
        y = player_rect.y
        w = player_rect.w
        h = player_rect.h
        if direction_list[2] == 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 12, y, w ,h), direction_list, skill_len, 10)
            rect3 = self.get_skill_1(pygame.Rect(x - 12, y, w ,h), direction_list, skill_len, 10)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
        elif direction_list[3] == 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x, y + 12, w ,h), direction_list, skill_len, 10)
            rect3 = self.get_skill_1(pygame.Rect(x, y - 12, w ,h), direction_list, skill_len, 10)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
        elif direction_list[2] * direction_list[3] > 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 8, y - 8, w ,h), direction_list, skill_len, 10)
            rect3 = self.get_skill_1(pygame.Rect(x - 8, y + 8, w ,h), direction_list, skill_len, 10)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
        elif direction_list[2] * direction_list[3] < 0:
            rect1 = self.get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
            rect2 = self.get_skill_1(pygame.Rect(x + 8, y + 8, w ,h), direction_list, skill_len, 10)
            rect3 = self.get_skill_1(pygame.Rect(x - 8, y - 8, w ,h), direction_list, skill_len, 10)
            for x in rect1:
                list_of_rectangles.append(x)
            for x in rect2:
                list_of_rectangles.append(x)
            for x in rect3:
                list_of_rectangles.append(x)
            
        return list_of_rectangles
            
    def get_skill_1(self, player_rect, direction_list, skill_len, start_len=3):
        list_of_rectangles = []
        if direction_list[0] == 0 and direction_list[1] == 0:
            for x in range(start_len, int(skill_len) + start_len):
                obj_rect = pygame.Rect(int(player_rect.centerx - self.skill_side / 2 + 5 * x * direction_list[2]),
                                       int(player_rect.centery - self.skill_side / 2 + 5 * x * direction_list[3]),
                                       self.skill_side,
                                       self.skill_side)
                list_of_rectangles.append(obj_rect)
        else:
            for x in range(start_len, int(skill_len) + start_len):
                obj_rect = pygame.Rect(int(player_rect.centerx - self.skill_side / 2 + 5 * x * direction_list[0]),
                                       int(player_rect.centery - self.skill_side / 2 + 5 * x * direction_list[1]),
                                       self.skill_side,
                                       self.skill_side)
                list_of_rectangles.append(obj_rect)
        return list_of_rectangles









    def game_over(self):
        self.hp = self.maxHp
        self.exp *= 0.8
        self.a_counter = 0
        self.a_image_couter = 1000
        self.phase = 1
        self.phase_counter = 0
        self.move_x_pos = self.screen_width / 2
        self.move_y_pos = self.screen_height / 2
        self.move_dx = 0
        self.move_dy = 0
        self.move_x_dir = 0
        self.move_y_dir = self.move_straight
        self.skill_a_use = False
        self.skill_s_use = False
        self.skill_d_use = False
        self.skill_f_use = False
        self.reload = False
        self.reload_counter = 0
        self.flagX = False
        self.temp_backX = 300000
        self.flagY = False
        self.temp_backY = 300000
        self.bullet = 6

        self.player_rect_object = pygame.Rect(int(self.move_x_pos),
                                           int(self.move_y_pos),
                                           self.player_width,
                                           self.player_height)

        self.skill_1_rect_object = self.get_skill_1(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_2_rect_object = self.get_skill_2(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_3_rect_object = self.get_skill_3(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)

    def game_win(self):
        self.hp = self.maxHp
        self.a_counter = 0
        self.a_image_couter = 1000
        self.phase = 1
        self.phase_counter = 0
        self.move_x_pos = self.screen_width / 2
        self.move_y_pos = self.screen_height / 2
        self.move_dx = 0
        self.move_dy = 0
        self.move_x_dir = 0
        self.move_y_dir = self.move_straight
        self.skill_a_use = False
        self.skill_s_use = False
        self.skill_d_use = False
        self.skill_f_use = False
        self.reload = False
        self.reload_counter = 0
        self.flagX = False
        self.temp_backX = 300000
        self.flagY = False
        self.temp_backY = 300000
        self.bullet = 6

        self.player_rect_object = pygame.Rect(int(self.move_x_pos),
                                           int(self.move_y_pos),
                                           self.player_width,
                                           self.player_height)

        self.skill_1_rect_object = self.get_skill_1(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_2_rect_object = self.get_skill_2(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)
        self.skill_3_rect_object = self.get_skill_3(self.player_rect_object,
                                               (self.move_dx, self.move_dy,
                                                self.move_x_dir, self.move_y_dir),
                                               self.player_range)

    # Logic - player
    def count_skill_a(self):
        self.a_counter += 1
        if self.a_counter > 35:
            self.a_counter -= 1

    def can_use_a(self):
        result = False
        if self.a_counter == 35:
            result = True
            self.a_counter = 0
            self.a_image_couter = 0
        return result

    def can_show_image_a(self):
        result = False
        if self.a_image_couter < 4:
            result = True
            self.a_image_couter += 1
        return result




    def increase_exp(self, exp_got):
        self.exp += exp_got
        if self.exp >= self.exp_required:
            self.exp -= self.exp_required
            self.exp_required = int(self.exp_required * 1.20)
            if self.level < 16:
                self.level += 1
        if self.exp >= self.exp_required:
            self.exp -= self.exp_required
            self.exp_required = int(self.exp_required * 1.20)
            if self.level < 16:
                self.level += 1
        if self.exp >= self.exp_required:
            self.exp -= self.exp_required
            self.exp_required = int(self.exp_required * 1.20)
            if self.level < 16:
                self.level += 1
        if self.level == 16 or self.exp < 0 or self.exp > self.exp_required:
            self.exp = 0


    def is_death(self):
        answer = False
        if self.hp <= 0:
            answer = True
        return answer

    def damaged_by(self, enemy, rect_list, damge_amount):
        if self.player_rect_object.collidelist(rect_list) >= 0 and damge_amount >= self.hp:
            self.hp = 0
        if self.player_rect_object.collidelist(rect_list) >= 0 and self.hp > 0:
            self.hp -= damge_amount










