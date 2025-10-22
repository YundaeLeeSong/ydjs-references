import pygame               # all available pygame submodules are automatically imported. - pygame Module
import math
import random
import time
import character
import enemy
import boss

## Note (what to adjust each time)
# 1. map size
# 2. background image and music
# 3. enemy members
# 4. Introduction
# 5. game win condition (comments)
# 6. game over condition (comments)




pygame.init()               # initialize all imported pygame modules (return: tuple). - pygame Module

# constants
const_screenWidth = 800
const_screenHeight = 560
const_background_size_x = 10
const_background_size_y = 10
const_random_list = [] 
for x in range(const_background_size_x * const_background_size_y):
    const_random_list.append(random.randrange(0, 4))

const_toolbar_width = 800
const_toolbar_height = 100

const_cylinder_width = 100
    
# screen
obj_screen = pygame.display.set_mode((const_screenWidth, const_screenHeight + const_toolbar_height)) # return a screen object (return: screen object) - pygame.display Module
pygame.display.set_caption('Golden Bullet')
obj_image_icon = pygame.image.load(r'pictures\icon.png').convert_alpha()
pygame.display.set_icon(obj_image_icon)

# Background Images
const_obj_image_loading_1 = pygame.image.load(r'pictures\loading_1.png').convert()
const_obj_image_loading_2 = pygame.image.load(r'pictures\loading_2.png').convert()
const_obj_image_loading_3 = pygame.image.load(r'pictures\loading_3.png').convert()

# button
obj_font_georgia_small = pygame.font.SysFont('georgia', 20)
button_surface = pygame.image.load(r'pictures\button_.png').convert()
button_surface_hover = pygame.image.load(r'pictures\button_hover_.png').convert()
button_w = 120
button_h = 60

# - tutorial & random battle
const_obj_image_presentation_tutorial = pygame.image.load(r'pictures\presentation_tutorial.png').convert()
const_obj_image_tutorial = pygame.image.load(r'pictures\background_tutorial.png').convert()



# - story 1
const_obj_image_presentation_1 = pygame.image.load(r'pictures\presentation_1.png').convert()
const_obj_image_1_1 = pygame.image.load(r'pictures\background_1_1.png').convert()
const_obj_image_1_2 = pygame.image.load(r'pictures\background_1_2.png').convert()
const_obj_image_1_3 = pygame.image.load(r'pictures\background_1_3.png').convert()

# - story 2
const_obj_image_presentation_2 = pygame.image.load(r'pictures\presentation_2.png').convert()
const_obj_image_2 = pygame.image.load(r'pictures\background_2.png').convert()

# - story 3
const_obj_image_presentation_3 = pygame.image.load(r'pictures\presentation_3.png').convert()
const_obj_image_3 = pygame.image.load(r'pictures\background_3.png').convert()
const_obj_image_the_world = pygame.image.load(r'pictures\shadow_background.png').convert()
const_obj_image_the_world_crack = pygame.image.load(r'pictures\shadow_background_2.png').convert_alpha()








const_toolbar_image = pygame.image.load(r'pictures\toolbar.png').convert()

const_cylinder_image_1 = pygame.image.load(r'pictures\cylinder_1.png').convert()
const_cylinder_image_2 = pygame.image.load(r'pictures\cylinder_2.png').convert()
const_cylinder_image_3 = pygame.image.load(r'pictures\cylinder_3.png').convert()
const_cylinder_image_4 = pygame.image.load(r'pictures\cylinder_4.png').convert()
const_cylinder_image_5 = pygame.image.load(r'pictures\cylinder_5.png').convert()
const_cylinder_image_6 = pygame.image.load(r'pictures\cylinder_6.png').convert()

const_skillbar_image_0 = pygame.image.load(r'pictures\skill_hidden_0.png').convert()
const_skillbar_image_1 = pygame.image.load(r'pictures\skill_hidden_1.png').convert()
const_skillbar_image_2 = pygame.image.load(r'pictures\skill_hidden_2.png').convert()
const_skillbar_image_3 = pygame.image.load(r'pictures\skill_hidden_3.png').convert()
const_skillbar_image_4 = pygame.image.load(r'pictures\skill_hidden_4.png').convert()



# Constants for Skill Images
obj_image_explosion_set_1 = pygame.image.load(r'pictures\explosion_1.png').convert_alpha()
obj_image_explosion_set_2 = pygame.image.load(r'pictures\explosion_2.png').convert_alpha()
obj_image_skill_3_1 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 0,0,16,16))####
obj_image_skill_3_2 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 1,0,16,16))####
obj_image_skill_3_3 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 2,0,16,16))####
obj_image_skill_3_4 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 3,0,16,16))####
obj_image_skill_3_5 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 4,0,16,16))####
obj_image_skill_3_6 = obj_image_explosion_set_2.subsurface(pygame.Rect(192 + 16 * 5,0,16,16))####
obj_image_skill_3_7 = obj_image_explosion_set_2.subsurface(pygame.Rect(415,0,33,33))####
obj_image_empty = obj_image_explosion_set_2.subsurface(pygame.Rect(0,30,30,30))####

obj_image_muda_skil = pygame.image.load(r'pictures\muda.png').convert_alpha()

obj_image_shadow = pygame.image.load(r'pictures\shadow.png').convert_alpha()



## Characters images
obj_image_char_set = pygame.image.load(r'pictures\sprite1.png').convert_alpha()
obj_image_char_set_modi = pygame.image.load(r'pictures\sprite2.png').convert_alpha()
obj_image_char_set_3 = pygame.image.load(r'pictures\sprite3.png').convert_alpha()
const_char_size = 32



# - 0. player (done)
obj_image_player_phase_1_list = []
for x in range(4):
    obj_image_player_phase_1_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 0),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_player_phase_2_list = []
for x in range(4):
    obj_image_player_phase_2_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 1),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_player_phase_3_list = []
for x in range(4):
    obj_image_player_phase_3_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 2),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))


# - 1. enemy (done)
obj_image_enemy_phase_1_list = []
for x in range(4):
    obj_image_enemy_phase_1_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 9 + const_char_size * 0),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_enemy_phase_2_list = []
for x in range(4):
    obj_image_enemy_phase_2_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 9 + const_char_size * 1),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_enemy_phase_3_list = []
for x in range(4):
    obj_image_enemy_phase_3_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 9 + const_char_size * 2),
                                                                                  int(const_char_size * 4 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

# - 2. Illene (Not done)
obj_image_illene_phase_1_list = []
for x in range(4):
    obj_image_illene_phase_1_list.append(obj_image_char_set_modi.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 0),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_illene_phase_2_list = []
for x in range(4):
    obj_image_illene_phase_2_list.append(obj_image_char_set_modi.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 1),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_illene_phase_3_list = []
for x in range(4):
    obj_image_illene_phase_3_list.append(obj_image_char_set_modi.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 2),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))


# - 3. Killer (done)
obj_image_killer_phase_1_list = []
for x in range(4):
    obj_image_killer_phase_1_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 3 + const_char_size * 0),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_killer_phase_2_list = []
for x in range(4):
    obj_image_killer_phase_2_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 3 + const_char_size * 1),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_killer_phase_3_list = []
for x in range(4):
    obj_image_killer_phase_3_list.append(obj_image_char_set.subsurface(pygame.Rect(int(const_char_size * 3 + const_char_size * 2),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

# - Boss (done)
obj_image_boss_phase_1_list = []
for x in range(4):
    obj_image_boss_phase_1_list.append(obj_image_char_set_3.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 0),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_boss_phase_2_list = []
for x in range(4):
    obj_image_boss_phase_2_list.append(obj_image_char_set_3.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 1),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

obj_image_boss_phase_3_list = []
for x in range(4):
    obj_image_boss_phase_3_list.append(obj_image_char_set_3.subsurface(pygame.Rect(int(const_char_size * 0 + const_char_size * 2),
                                                                                  int(const_char_size * 0 + const_char_size * x),
                                                                                  int(const_char_size),
                                                                                  int(const_char_size))))

# Skill Sounds
const_sound_skill_a = r'sounds\skill_1.wav'
const_sound_skill_s = r'sounds\skill_2.wav'
const_sound_skill_d = r'sounds\skill_3.wav'
const_sound_skill_f = r'sounds\skill_4.wav'
const_sound_reload = r'sounds\reload.wav'
const_sound_yeeha = r'sounds\yeeha.wav'

const_sound_the_world = r'sounds\the_world.wav'
const_sound_muda = r'sounds\muda.wav'

# text box image
const_text_box_image = pygame.image.load(r'pictures\text_box.png').convert()

# button image




# objects etc...
obj_clock = pygame.time.Clock()
obj_font_impact = pygame.font.SysFont('impact', 25)
obj_font_georgia = pygame.font.SysFont('georgia', 25)
obj_font_big_impact = pygame.font.SysFont('impact', 40)




def show_image_by_coordinate(image, x, y):
    image_rect = image.get_rect() # get_rect() returns a rectangle has same width and height as surface
    image_rect.center = (int(x), int(y)) # center the message!! (destination)
    obj_screen.blit(image, image_rect)


def good_message(string, num_of_line): 
    obj_surface_text = obj_font_impact.render(string, True, pygame.Color(0, 0, 0))
    obj_surface_big_text = obj_font_big_impact.render(string, True, pygame.Color(0, 255, 0))
    
    if num_of_line == 1:
        obj_screen.fill(pygame.Color(255, 255, 255))
    if num_of_line == 1:
        show_image_by_coordinate(obj_surface_big_text, const_screenWidth / 2, const_screenHeight / 2 - 20)
    if num_of_line == 2:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 30)
    if num_of_line == 3:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 60)
    if num_of_line == 4:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 90)






# Background Music
const_music_main_theme = r'sounds\main_theme.mp3'
const_music_main_theme_2 = r'sounds\main_theme_2.mp3'
const_music_background_1 = r'sounds\background_1.mp3'
const_music_background_2 = r'sounds\background_2.mp3'
const_music_background_3 = r'sounds\background_3.mp3'
const_music_story_1 = r'sounds\story_1.mp3'
const_music_story_2 = r'sounds\story_2.mp3'
const_music_boss = r'sounds\boss.mp3'
    

def main(character_player):
    # Background Music
    play_background_music(const_music_main_theme_2)
    
    # Variables for keyboard input
    var_gameExit = False
    var_gameover = False
    var_gamewin = False
    var_FPS = 120
    dx = 0
    dy = 0

    # background beginning position
    n_x = 0 # right: 0, left: const_background_size_x - 1
    n_y = 0 # bottom: 0, top: const_background_size_y - 1
    back_x = const_screenWidth * n_x
    back_y = const_screenHeight * n_y



    # Enemy Objects
    ##############################
    enemy_list = []
    num_enemy = random.randrange(20, 30)
    for x in range(num_enemy):
        enemy_member = enemy.Enemy(const_screenWidth, const_screenHeight,
                          const_background_size_x, const_background_size_y,
                          back_x, back_y)
        enemy_list.append(enemy_member)
        
    # Illene Objects
    ##############################
    illene_list = []
    num_enemy = random.randrange(20, 30)
    for x in range(num_enemy):
        illene_member = enemy.Illene(const_screenWidth, const_screenHeight,
                          const_background_size_x, const_background_size_y,
                          back_x, back_y)
        illene_list.append(illene_member)

    # Killer Objects
    ##############################
    killer_list = []
    num_enemy = random.randrange(20, 30)
    for x in range(num_enemy):
        killer_member = enemy.Killer(const_screenWidth, const_screenHeight,
                          const_background_size_x, const_background_size_y,
                          back_x, back_y)
        killer_list.append(killer_member)

    # Boss Objects
    ##############################
    boss_object_1 = boss.Boss(const_screenWidth, const_screenHeight,
                            const_background_size_x, const_background_size_y,
                            back_x, back_y)
    boss_object_1.hp = 1000
    boss_object_1.exp = 500
    boss_exist = False
    if boss_exist:
        boss_object_1.hp = boss_object_1.hp
    else:
        boss_object_1.hp = 0






    # Introduction
    loading_background()
    if not character_player.seen_intro_random:
        presentation(const_obj_image_presentation_tutorial)
        conversation('Illene: ',
                     'Hey Mista, you come to this place again',
                     'Do you think you are weak yet?')
        conversation('Illene: ',
                     'As I already mentioned!',
                     'This virtual system will help you to gain more power.')
        conversation('Illene: ',
                     'Here, you can literally experience everything',
                     'before you get to the missions.')
        conversation('Illene: ',
                     'However, training is just training.',
                     'They are weaker than the actual guys.')
        conversation('Illene: ',
                     "Don't forget the fact when you proceed ",
                     "the story mode!")
        conversation('Illene: ',
                     "Then, good luck!")
        conversation('Illene: ',
                     "Ah! and you can exit the game whenever you want.",
                     "There is no penalty!!")
        character_player.seen_intro_random = True

    conversation('Mission Object: ',
                 "1. Defeat all the enemies")

    ################################# Game Loop #################################
    while not var_gameExit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second


        
        # (!) Game Over Loop (all different) #####################################################################
        if character_player.is_death():
            conversation('Mista: ',
                         "Damn... I need more train..")
            conversation('Sexy pistols: ',
                         "Mista!! show your effort more!")
            conversation('Mista: ',
                         "...")
            conversation('Mista: ',
                         "shut up..")

            character_player.game_win()
            var_gameover = True
        while var_gameover:
            alert_message('Train is Over', 1)
            alert_message('What to do next?', 2)
            alert_message('Press C to train again', 3)
            alert_message('Press Q to quit the virtual system', 4)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        var_gameover = False
                        var_gameExit = True
                    if event.key == pygame.K_c:
                        main(character_player)


                        
        # (!) Game Win Loop (all different) #####################################################################
        if is_list_death(enemy_list) and boss_object_1.is_death() and is_list_death(illene_list) and is_list_death(killer_list):
            conversation('Mista: ',
                         "Damn... I got this!")
            conversation('Sexy pistols: ',
                         "Mista!! it is about to be the time to kill DIO")
            conversation('Mista: ',
                         "Yeah, love you, sexy pistols")

            character_player.game_win()
            var_gamewin = True
        while var_gamewin:
            good_message('Train Complete', 1)
            good_message('', 2)
            good_message('congulatulations!', 3)
            good_message('You defeat all the enemies!', 4)
            pygame.display.update()

            time.sleep(1.5)
            var_gamewin = False
            var_gameExit = True




        

        
        ###### keyboard input (INPUT) ######
        # Input - player
        for obj_event in pygame.event.get():
            # exit
            if obj_event.type == pygame.QUIT:       
                quit()
            # keydown
            if obj_event.type == pygame.KEYDOWN:
                if obj_event.key == pygame.K_LEFT:
                    dx = -2
                if obj_event.key == pygame.K_RIGHT:
                    dx = 2
                if obj_event.key == pygame.K_UP:
                    dy = -2
                if obj_event.key == pygame.K_DOWN:
                    dy = 2
                if obj_event.key == pygame.K_a:
                    character_player.skill_a_use = True
                if obj_event.key == pygame.K_s:
                    character_player.skill_s_use = True
                if obj_event.key == pygame.K_d:
                    character_player.skill_d_use = True
                if obj_event.key == pygame.K_f:
                    character_player.skill_f_use = True
                if obj_event.key == pygame.K_r:
                    if character_player.bullet != 6:
                        character_player.reload = True
                if obj_event.key == pygame.K_SPACE:
                    var_FPS = 240
                        
            # keyup
            if obj_event.type == pygame.KEYUP:
                if obj_event.key == pygame.K_LEFT or obj_event.key == pygame.K_RIGHT:
                    dx = 0
                if obj_event.key == pygame.K_UP or obj_event.key == pygame.K_DOWN:
                    dy = 0
                if obj_event.key == pygame.K_a:
                    character_player.skill_a_use = False
                if obj_event.key == pygame.K_s:
                    character_player.skill_s_use = False
                if obj_event.key == pygame.K_d:
                    character_player.skill_d_use = False
                if obj_event.key == pygame.K_f:
                    character_player.skill_f_use = False
                if obj_event.key == pygame.K_r:
                    character_player.reload = False
                if obj_event.key == pygame.K_SPACE:
                    var_FPS = 120
                    
        skill_open_2(character_player)
        skill_open_3(character_player)
        skill_open_4(character_player)
        
        if boss_exist and boss_object_1.is_THE_WORLD(): # (special) T.H.E. W.O.R.L.D. Skill
            dx = 0
            dy = 0
            var_FPS = 120
            character_player.skill_a_use = False
            character_player.skill_s_use = False
            character_player.skill_d_use = False
            character_player.skill_f_use = False
            character_player.reload = False
            
        #else:
            #resume_background_music()


        ###### Action Settings (PROCESS) ######
        # action - player
        character_player.make_movement(dx, dy, back_x, const_background_size_x, back_y, const_background_size_y)
        back_x, back_y = set_background(back_x, back_y, character_player.back_dx, character_player.back_dy)
        
        # action ----- enemies
        for x in range(len(enemy_list)):
            make_movement(enemy_list[x], back_x, back_y)
            
        for x in range(len(illene_list)):
            make_movement(illene_list[x], back_x, back_y)
            
        for x in range(len(killer_list)):
            make_movement(killer_list[x], back_x, back_y)

        #if boss_exist: 
            #make_movement(boss_object_1, back_x, back_y) # normal boss movement

        if boss_exist: # special boss movement
            boss_object_1.make_movement_to_player(back_x, back_y, character_player.get_player_rect())




        ####################################### Display results (OUTPUT) ######
        # screen - draw background
        show_one_background(back_x, back_y, const_obj_image_tutorial)





        # screen ----- draw enemies
        ##############################
        for x in range(len(enemy_list)):
            if not enemy_list[x].is_death():
                show_image_by_rect(determine_image_direction(enemy_list[x],
                                                             image_phase(enemy_list[x],
                                                                         obj_image_enemy_phase_1_list,
                                                                         obj_image_enemy_phase_2_list,
                                                                         obj_image_enemy_phase_3_list)),
                                   enemy_list[x].get_enemy_rect())

                
        for x in range(len(illene_list)):
            if not illene_list[x].is_death():
                show_image_by_rect(determine_image_direction((illene_list[x]),
                                                             image_phase((illene_list[x]),
                                                                         obj_image_illene_phase_1_list,
                                                                         obj_image_illene_phase_2_list,
                                                                         obj_image_illene_phase_3_list)),
                                   illene_list[x].get_enemy_rect())


        for x in range(len(killer_list)):
            if not killer_list[x].is_death():
                show_image_by_rect(determine_image_direction((killer_list[x]),
                                                             image_phase((killer_list[x]),
                                                                         obj_image_killer_phase_1_list,
                                                                         obj_image_killer_phase_2_list,
                                                                         obj_image_killer_phase_3_list)),
                                   killer_list[x].get_enemy_rect())
                
        for x in range(len(killer_list)):
            if not killer_list[x].is_death():
                show_shadow(obj_image_shadow, killer_list[x].get_shadow())



        if boss_exist and (not boss_object_1.is_death()):
            show_image_by_rect(determine_image_direction(boss_object_1,
                                                         image_phase(boss_object_1,
                                                                     obj_image_boss_phase_1_list,
                                                                     obj_image_boss_phase_2_list,
                                                                     obj_image_boss_phase_3_list)),
                               boss_object_1.get_enemy_rect())


        # screen - draw player
        show_image_by_rect(determine_image_direction(character_player,
                                                     image_phase(character_player,
                                                                 obj_image_player_phase_1_list,
                                                                 obj_image_player_phase_2_list,
                                                                 obj_image_player_phase_3_list)),
                           character_player.get_player_rect())
        








        # screen - interface
        show_interface(character_player, character_player.level, character_player.bullet)

        character_player.count_skill_a()

        # screen - skill use
        if character_player.skill_a_use and character_player.bullet >= 1 and character_player.level >= 1 and character_player.can_use_a():
            skill_a(character_player, enemy_list, illene_list, killer_list, boss_object_1)
        if character_player.skill_s_use and character_player.bullet >= 3 and character_player.level >= 6:
            skill_s(character_player, enemy_list, illene_list, killer_list, boss_object_1)
        if character_player.skill_d_use and character_player.bullet >= 5 and character_player.level >= 11:
            skill_d(character_player, enemy_list, illene_list, killer_list, boss_object_1)
        if character_player.skill_f_use and character_player.bullet >= 6 and character_player.level >= 16:
            skill_f(character_player, enemy_list, illene_list, killer_list, boss_object_1)
        if character_player.reload: # reload
            reload(character_player)

        if character_player.can_show_image_a():
            show_image_by_rect_list(generate_image_list(character_player.get_skill_1_rect(), obj_image_skill_3_4, 10),
                                character_player.get_skill_1_rect())
            


        # screen - skill uses (Enemies)
        ##############################
        for x in range(len(enemy_list)):
            if not enemy_list[x].is_death():
                enemy_list[x].catch(character_player)
                
        for x in range(len(killer_list)):
            if not killer_list[x].is_death():
                killer_list[x].catch(character_player)




        if boss_exist and (not boss_object_1.is_death()):
            boss_object_1.catch(character_player)
            
        if boss_exist and (not boss_object_1.is_death()):
            if boss_object_1.is_use_THE_WORLD():
                play_wav_sound(const_sound_the_world)
                #pause_background_music()
        
        if boss_exist and (not boss_object_1.is_death()):
            boss_object_1.count_muda()
            if boss_object_1.can_muda(character_player.get_player_rect()):
                if boss_object_1.is_muda():
                    skill_muda(boss_object_1, character_player)

        button('Exit', 740, 530)
        if is_click_button(740, 530):
            conversation('Quit the game...')

            character_player.game_win()
            var_gameExit = True

    return character_player





def skill_a(character_player, enemy_list, illene_list, killer_list, boss_object_1):
    play_wav_sound(const_sound_skill_a)  # skill a sound

    character_player.use_bullet()
    show_cylinder(character_player.bullet)

    show_image_by_rect_list(generate_image_list(character_player.get_skill_1_rect(), obj_image_skill_3_4, 10),
                            character_player.get_skill_1_rect())

    show_interface(character_player, character_player.level, character_player.bullet)

    for x in range(len(enemy_list)):
        enemy_list[x].damaged_by(character_player, character_player.get_skill_1_rect(),
                                 character_player.get_skill_1_damage())
    for x in range(len(illene_list)):
        illene_list[x].damaged_by(character_player, character_player.get_skill_1_rect(),
                                  character_player.get_skill_1_damage())
    for x in range(len(killer_list)):
        killer_list[x].damaged_by(character_player, character_player.get_skill_1_rect(),
                                  character_player.get_skill_1_damage())
    boss_object_1.damaged_by(character_player, character_player.get_skill_1_rect(),
                             character_player.get_skill_1_damage())

    pygame.display.update()


























def is_click_button(x, y):  # event_handler
    result = False

    cursur = pygame.mouse.get_pos()
    mouse_action = pygame.mouse.get_pressed()

    if abs(cursur[0] - x) <= button_w / 2 and abs(cursur[1] - y) <= button_h / 2 and mouse_action[0] == 1:
        result = True
    else:
        result = False
    return result


def button(string, x, y):
    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= button_w / 2 and abs(cursur[1] - y) <= button_h / 2:
        show_image_by_coordinate(button_surface_hover, x, y)
    else:
        show_image_by_coordinate(button_surface, x, y)

    button_message(string, x, y)


def button_message(string, x, y):
    text_surface = obj_font_georgia_small.render(string, True, pygame.Color(0, 0, 0))
    text_surface_hover = obj_font_georgia_small.render(string, True, pygame.Color(255, 255, 255))

    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= button_w / 2 and abs(cursur[1] - y) <= button_h / 2:
        show_image_by_coordinate(text_surface_hover, x, y)
    else:
        show_image_by_coordinate(text_surface, x, y)



def skill_open_2(character_player):
    if character_player.level == 6 and character_player.skill2_notice == False:
        conversation('Mista: ',
                     'Great, now I feel stronger power on my revolver.')
        conversation('Mista: ',
                     'Great, now I feel stronger power on my revolver.',
                     "Let's try to shoot in a new way!")
        conversation('Mista: ',
                     'Great, now I feel stronger power on my revolver.',
                     "Let's try to shoot in a new way!",
                     '(Press S key to shoot 1-2 bullets)')
        character_player.skill2_notice = True


def skill_open_3(character_player):
    if character_player.level == 11 and character_player.skill3_notice == False:
        conversation('Mista: ',
                     'What..? what is this?')
        conversation('Pistols: ',
                     'Hey mista, now you can shoot more than 3 times',
                     "Use us to defeat stronger enemies!")
        conversation('Mista: ',
                     'Ok, my sexy pistols',
                     "Let's go",
                     '(Press D key to shoot 5 consecutive bullets)')
        character_player.skill3_notice = True



def skill_open_4(character_player):
    if character_player.level == 16 and character_player.skill4_notice == False:
        conversation('Pistols: ',
                     'Hey mista')
        conversation('Pistols: ',
                     'Hey mista',
                     "It's time to awaken us one more.")
        conversation('Pistols: ',
                     'Hey mista',
                     "It's time to awaken us one more",
                     'You finally changed us to requiem mode')
        conversation('Pistols: ',
                     'Hey mista',
                     "It's time to awaken us one more",
                     'You finally changed us to requiem mode',
                     'It will be the strongest one you will ever experience',
                     '(Press F key to use "Final Shot")')
        character_player.skill4_notice = True







# For images on skills and characters
def show_rect(rect):
    color1 = random.randrange(0, 255)
    color2 = random.randrange(0, 255)
    color3 = random.randrange(0, 255)
    pygame.draw.rect(obj_screen, (color1, color2, color3), rect)

def show_shadow(image, rect):
    obj_screen.blit(image, [rect.x, rect.y])
    
def show_image_by_rect(image, rect): # centered!
    image_rect = image.get_rect() 
    image_rect.centerx = rect.centerx
    image_rect.centery = rect.centery
    obj_screen.blit(image, image_rect)

def image_phase(obj, image_list1, image_list2, image_list3):
    image_list = []
    if obj.phase == 1:
        image_list = image_list1
    elif obj.phase == 2:
        image_list = image_list2
    elif obj.phase == 3:
        image_list = image_list3
    return image_list

def determine_image_direction(obj, image_list):
    image_to_return = 0
    if abs(obj.move_x_dir) < 0.5 and obj.move_y_dir > 0: 
        image_to_return = image_list[0] ## down
    elif abs(obj.move_x_dir) < 0.5 and obj.move_y_dir < 0:
        image_to_return = image_list[3] ## up
    elif obj.move_x_dir <= 0.5: 
        image_to_return = image_list[1] ## left
    elif obj.move_x_dir >= 0.5: 
        image_to_return = image_list[2] ## right

    return image_to_return
    



## For button
def show_centered_image(image):
    image_rect = image.get_rect()
    image_rect.center = (int(const_screenWidth / 2), int(const_screenHeight / 2))
    obj_screen.blit(image, image_rect)



# Muda Muda Muda

def show_image_on_rec(image, boss_object):
    x = boss_object.get_muda_x() + random.randrange(-50, 51)
    y = boss_object.get_muda_y() + random.randrange(-50, 51)
    
    obj_screen.blit(image, [x, y])


def skill_muda(boss_object, character_player):
    if boss_object.muda_counter == 5480:
        play_wav_sound(const_sound_muda)
    show_image_on_rec(modify_muda(boss_object), boss_object)
    skill = []
    skill.append(boss_object.get_skill_muda())
    character_player.damaged_by(boss_object, skill, boss_object.get_skill_muda_damage())


def modify_muda(boss_object):
    if boss_object.move_y_dir < 0 and boss_object.move_x_dir > 0:
        image = pygame.transform.rotate(obj_image_muda_skil, math.degrees(0 + abs(math.atan(boss_object.move_y_dir / boss_object.move_x_dir))))
    elif boss_object.move_y_dir < 0 and boss_object.move_x_dir < 0:
        image = pygame.transform.rotate(obj_image_muda_skil, math.degrees(90 + abs(math.atan(boss_object.move_x_dir / boss_object.move_y_dir))))
    elif boss_object.move_y_dir > 0 and boss_object.move_x_dir < 0:
        image = pygame.transform.rotate(obj_image_muda_skil, math.degrees(110 + abs(math.atan(boss_object.move_y_dir / boss_object.move_x_dir))))
    elif boss_object.move_y_dir > 0 and boss_object.move_x_dir > 0:
        image = pygame.transform.rotate(obj_image_muda_skil, math.degrees(200 + abs(math.atan(boss_object.move_x_dir / boss_object.move_y_dir))))
    return image








def show_the_world_background(x, y, image1):
    for n_x in range(const_background_size_x):
        for n_y in range(const_background_size_y):
            obj_screen.blit(image1, [int(-const_screenWidth * (n_x) + x), int(-const_screenHeight * (n_y) + y)])
    obj_screen.blit(const_obj_image_the_world_crack, [int(const_screenWidth / 2), int(const_screenHeight / 2)])
    obj_screen.blit(const_obj_image_the_world_crack, [int(const_screenWidth / 2 - 300), int(const_screenHeight / 2 - 100)])
    obj_screen.blit(const_obj_image_the_world_crack, [int(const_screenWidth / 2 - 100), int(const_screenHeight / 2 - 250)])
    obj_screen.blit(const_obj_image_the_world_crack, [int(const_screenWidth / 2 - 500), int(const_screenHeight / 2 - 500)])
    obj_screen.blit(const_obj_image_the_world_crack, [int(const_screenWidth / 2 + 100), int(const_screenHeight / 2 + 250)])



def show_one_background(x, y, image1):
    for n_x in range(const_background_size_x):
        for n_y in range(const_background_size_y):
            obj_screen.blit(image1, [int(-const_screenWidth * (n_x) + x), int(-const_screenHeight * (n_y) + y)])


def show_background(x, y, image1, image2, image3):
    counter = 0
    for n_x in range(const_background_size_x):
        for n_y in range(const_background_size_y):
            if const_random_list[counter] <= 1:
                obj_screen.blit(image1,
                                [int(-const_screenWidth * (n_x) + x),
                                 int(-const_screenHeight * (n_y) + y)])
            if const_random_list[counter] == 2:
                obj_screen.blit(image2,
                                [int(-const_screenWidth * (n_x) + x),
                                 int(-const_screenHeight * (n_y) + y)])
            if const_random_list[counter] == 3:
                obj_screen.blit(image3,
                                [int(-const_screenWidth * (n_x) + x),
                                 int(-const_screenHeight * (n_y) + y)])
            counter += 1









def loading_background():
    obj_screen.fill(pygame.Color(255, 255, 255), pygame.Rect(0,0,const_screenWidth, const_screenHeight + const_toolbar_height))
    obj_screen.blit(const_obj_image_loading_1, [0, 0])
    pygame.display.update()
    time.sleep(0.6)
    obj_screen.blit(const_obj_image_loading_2, [0, 0])
    pygame.display.update()
    time.sleep(0.6)
    obj_screen.blit(const_obj_image_loading_3, [0, 0])
    pygame.display.update()
    time.sleep(0.6)

def presentation(image):
    obj_screen.blit(image, [0, 0])
    pygame.display.update()
    time.sleep(2)


def alert_message(string, num_of_line): 
    obj_surface_text = obj_font_impact.render(string, True, pygame.Color(255, 255, 255))
    obj_surface_big_text = obj_font_big_impact.render(string, True, pygame.Color(255, 0, 0))
    
    if num_of_line == 1:
        obj_screen.fill(pygame.Color(0, 0, 0))
    if num_of_line == 1:
        show_image_by_coordinate(obj_surface_big_text, const_screenWidth / 2, const_screenHeight / 2 - 20)
    if num_of_line == 2:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 30)
    if num_of_line == 3:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 60)
    if num_of_line == 4:
        show_image_by_coordinate(obj_surface_text, const_screenWidth / 2, const_screenHeight / 2 + 90)





def conversation(string1='', string2='', string3='', string4='', string5='', string6='', string7='', string8=''):
    conv = True
    while conv:
        alert_box_message(string1, 1)
        alert_box_message(string2, 2)
        alert_box_message(string3, 3)
        alert_box_message(string4, 4)
        alert_box_message(string5, 5)
        alert_box_message(string6, 6)
        alert_box_message(string7, 7)
        alert_box_message(string8, 8)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    conv = False

def alert_box_message(string, num_of_line):
    obj_surface_text = obj_font_georgia.render(string, True, pygame.Color(255, 255, 255))
    
    if num_of_line == 1:
        obj_screen.blit(const_text_box_image, [int(100), int(100)]) # box
    if num_of_line == 1:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 0)])
    if num_of_line == 2:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 1)])
    if num_of_line == 3:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 2)])
    if num_of_line == 4:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 3)])
    if num_of_line == 5:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 4)])
    if num_of_line == 6:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 5)])
    if num_of_line == 7:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 6)])
    if num_of_line == 8:
        obj_screen.blit(obj_surface_text, [int(100 + 10), int(100 + 10 + 30 * 7)])


def reload(character_player):
    if character_player.can_reload():
        play_wav_sound(const_sound_reload)
        character_player.reload_bullet()
        show_cylinder(character_player.bullet)
        pygame.display.update()


def show_interface(character_player, level, bullet):
    show_toolbar(character_player)
    show_skillbar(level)
    show_cylinder(bullet)
    show_level(character_player)

def show_toolbar(player):
    obj_screen.blit(const_toolbar_image, [0, const_screenHeight])
    pygame.draw.rect(obj_screen, (200, 0, 0), pygame.Rect(405, const_screenHeight + 8, int(200 * player.hp / player.maxHp), 30))
    pygame.draw.rect(obj_screen, (255, 255, 0), pygame.Rect(405, const_screenHeight + 58, int(200 * player.exp / player.exp_required), 30))

def show_skillbar(num):
    if num == 16:
        obj_screen.blit(const_skillbar_image_0, [0, const_screenHeight])
    elif num >= 11:
        obj_screen.blit(const_skillbar_image_1, [0, const_screenHeight])
    elif num >= 6:
        obj_screen.blit(const_skillbar_image_2, [0, const_screenHeight])
    else:
        obj_screen.blit(const_skillbar_image_3, [0, const_screenHeight])

def show_cylinder(num):
    if num == 6:
        obj_screen.blit(const_cylinder_image_6, [const_screenWidth - const_cylinder_width, const_screenHeight])
    elif num == 5:
        obj_screen.blit(const_cylinder_image_5, [const_screenWidth - const_cylinder_width, const_screenHeight])
    elif num == 4:
        obj_screen.blit(const_cylinder_image_4, [const_screenWidth - const_cylinder_width, const_screenHeight])
    elif num == 3:
        obj_screen.blit(const_cylinder_image_3, [const_screenWidth - const_cylinder_width, const_screenHeight])
    elif num == 2:
        obj_screen.blit(const_cylinder_image_2, [const_screenWidth - const_cylinder_width, const_screenHeight])
    elif num == 1:
        obj_screen.blit(const_cylinder_image_1, [const_screenWidth - const_cylinder_width, const_screenHeight])

def show_level(player):
    obj_surface_text = obj_font_impact.render(str(player.level), True, pygame.Color(0, 0, 0))
    show_image_by_coordinate(obj_surface_text, const_screenWidth - 144, const_screenHeight + 74)


def play_background_music(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.35)
    pygame.mixer.music.play(-1)

def pause_background_music():
    pygame.mixer.music.pause()

def resume_background_music():
    pygame.mixer.music.unpause()

def play_wav_sound(filename):
    sound = pygame.mixer.Sound(filename)
    sound.set_volume(1)
    sound.play()

def set_background(x, y, dx, dy):
    x += dx
    y += dy
    if (-const_screenWidth * (const_background_size_x - 1) + x > 0
        or x < 0):
        x -= dx
    if (-const_screenHeight * (const_background_size_y - 1) + y > 0
        or y < 0):
        y -= dy
    return (x, y)


def make_movement(enemy_1, back_x, back_y):
    if enemy_1.get_counter() > 100:
        enemy_1.reset_pattern()

    if enemy_1.get_pattern() >= 80:
        enemy_1.make_movement1(back_x, back_y)
    elif enemy_1.get_pattern() > 60:
        enemy_1.make_movement2(back_x, back_y)
    elif enemy_1.get_pattern() > 40:
        enemy_1.make_movement3(back_x, back_y)
    elif enemy_1.get_pattern() > 20:
        enemy_1.make_movement4(back_x, back_y)
    else:
        enemy_1.make_movement5(back_x, back_y)




def is_list_death(enemy_list):
    result = True
    for x in range(len(enemy_list)):
        result = result and enemy_list[x].is_death()
    return result








def skill_s(character_player, enemy_list, illene_list, killer_list, boss_object_1):
    play_wav_sound(const_sound_skill_s) # skill s sound

    character_player.use_bullet()
    show_cylinder(character_player.bullet)
    
    show_image_by_rect_list(generate_image_list(character_player.get_skill_1_rect(), obj_image_skill_3_3, 10), character_player.get_skill_1_rect())
    
    show_interface(character_player, character_player.level, character_player.bullet)

    
    for x in range(len(enemy_list)):
        enemy_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    for x in range(len(illene_list)):
        illene_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    for x in range(len(killer_list)):
        killer_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
        
    boss_object_1.damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    
    pygame.display.update()
    time.sleep(character_player.get_s1_delay())  # skill s delay

    for num in range(2):
        character_player.use_bullet()
        show_cylinder(character_player.bullet)
        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_7, 10), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 2)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 2)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 2)
        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 2)
        
        pygame.display.update()
        time.sleep(character_player.get_s2_delay() / 2)  # skill s delay




def skill_d(character_player, enemy_list, illene_list, killer_list, boss_object_1):
    play_wav_sound(const_sound_skill_d) # skill d sound

    for num in range(5):
        character_player.use_bullet()
        show_cylinder(character_player.bullet)
        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_1, 5), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        
        pygame.display.update()
        time.sleep(character_player.get_d_delay() / 5) # skill d delay


        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_2, 5), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        
        pygame.display.update()
        time.sleep(character_player.get_d_delay() / 5) # skill d delay


        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_3, 5), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        
        pygame.display.update()
        time.sleep(character_player.get_d_delay() / 5) # skill d delay


        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_6, 10), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        
        pygame.display.update()
        time.sleep(character_player.get_d_delay() / 5) # skill d delay


        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_2_rect(), obj_image_skill_3_7, 15), character_player.get_skill_2_rect())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
            

        boss_object_1.damaged_by(character_player, character_player.get_skill_2_rect(), character_player.get_skill_2_damage() / 5)
        
        pygame.display.update()
        time.sleep(character_player.get_d_delay() / 5 - 0.05) # skill d delay
        



def skill_f(character_player, enemy_list, illene_list, killer_list, boss_object_1):
    play_wav_sound(const_sound_skill_f) # skill f sound
    
    for num in range(6):
        character_player.use_bullet()
        show_cylinder(character_player.bullet)

        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_1, 10),
                                character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep(character_player.get_f_delay() / 6)





        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_2, 10),
                                character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep(character_player.get_f_delay() / 6)




        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_3, 10),
                                character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep(character_player.get_f_delay() / 6)




        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_4, 10),
                                character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep(character_player.get_f_delay() / 6)




        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_5, 15),
                                character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
            
        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep(character_player.get_f_delay() / 6)



        
        
        show_image_by_rect_list(generate_image_list(character_player.get_skill_3_rect(), obj_image_skill_3_7, 10),
                                    character_player.get_skill_3_rect())#####################
        
        show_interface(character_player, character_player.level, character_player.bullet)
        
        for x in range(len(enemy_list)):
            enemy_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(illene_list)):
            illene_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        for x in range(len(killer_list)):
            killer_list[x].damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)

        boss_object_1.damaged_by(character_player, character_player.get_skill_3_rect(), character_player.get_skill_3_damage() / 6)
        
        pygame.display.update()
        time.sleep((character_player.get_f_delay() - 0.125) / 6) # skill f delay
        
    play_wav_sound(const_sound_yeeha)
    #show_rect(rect_list_to_rect()) ===== show_rect_list()         character_player.get_skill_3_rect()

def show_rect_list(rect_list):
    for x in range(len(rect_list)):
        color1 = random.randrange(0, 255)
        color2 = random.randrange(0, 255)
        color3 = random.randrange(0, 255)
        pygame.draw.rect(obj_screen, pygame.Color(color1, color2, color3), rect_list[x])
    pygame.display.update()

def generate_image_list(rect_list, image, num_image):
    image_list = [obj_image_empty] * len(rect_list)
    for index in range(num_image):
        num = random.randrange(len(rect_list))
        image_list[num] = image
    return image_list

def show_image_by_rect_list(image_list, rect_list): # centered!
    image_list_rect = []
    for n in range(len(image_list)):
        image_list_rect.append(image_list[n].get_rect()) 
        image_list_rect[n].center = rect_list[n].center 
        obj_screen.blit(image_list[n], image_list_rect[n])
    pygame.display.update()


