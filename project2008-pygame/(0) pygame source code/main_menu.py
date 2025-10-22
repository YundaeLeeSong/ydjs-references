import pygame               # all available pygame submodules are automatically imported. - pygame Module
import math
import random
import time
import character
import enemy
import boss
import tutorial
import story1
import story2
import story3
import random_battle

## Note (what to adjust each time)
# 1. map size
# 2. background image and music
# 3. Introduction

# 4. enemy
# 5. game win condition
# 6. game over condition




pygame.init()               # initialize all imported pygame modules (return: tuple). - pygame Module

# constants
const_screenWidth = 800
const_screenHeight = 560
const_background_size_x = 2
const_background_size_y = 2
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



# objects etc...
obj_clock = pygame.time.Clock()
obj_font_georgia_small = pygame.font.SysFont('georgia', 20)
obj_font_impact = pygame.font.SysFont('impact', 25)
obj_font_georgia = pygame.font.SysFont('georgia', 25)
obj_font_big_impact = pygame.font.SysFont('impact', 40)




# Background Images
main_surface = pygame.image.load(r'pictures\main_menu.png').convert()
main_surface_2 = pygame.image.load(r'pictures\main_menu_2.png').convert()
const_text_box_image = pygame.image.load(r'pictures\text_box.png').convert()


# Background Sounds



# button image
button_lock_surface = pygame.image.load(r'pictures\button_lock.png').convert_alpha()

button_surface = pygame.image.load(r'pictures\button.png').convert()
button_surface_hover = pygame.image.load(r'pictures\button_hover.png').convert()

large_button_surface = pygame.image.load(r'pictures\long_button.png').convert()
large_button_surface_hover = pygame.image.load(r'pictures\long_button_hover.png').convert()

char_button_surface = pygame.image.load(r'pictures\char_selection_1.jpg').convert()
char_button_surface_hover = pygame.image.load(r'pictures\char_selection_1_hover.jpg').convert()

char_button_surface_2 = pygame.image.load(r'pictures\char_selection_2.jpg').convert()

# button constants
button_w = 200
button_h = 100
large_button_w = 400
large_button_h = 100
char_button_w = 300
char_button_h = 400





# Background Music
const_music_main_theme_2 = r'sounds\main_theme_2.mp3'
const_music_main_theme = r'sounds\main_theme.mp3'
pygame.mixer.music.load(const_music_main_theme)
pygame.mixer.music.set_volume(0.35)





def main_menu():
    random_battle.alert_message('(!) Notice', 1)
    random_battle.alert_message('This game includes a lot of JJBA references', 2)
    random_battle.alert_message('but the game does not intend to break the copyright law.', 3)
    random_battle.alert_message('It will be used only for the submission of pygame project in CIST 2742.', 4)
    pygame.display.update()
    time.sleep(10)
    pygame.mixer.music.play(-1)

    # FPS
    menu_exit = False
    var_FPS = 15
    ################################# Main Menu #################################
    while not menu_exit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                    
        ## Menu Background
        if True:
            obj_screen.blit(main_surface, [0, 0])
        
        ############## Buttons Settings ##############
        if True: # main menu
            button('Start', 200, 600)
            if is_click_button(200, 600):
                char_selection()

        button('Quit', 600, 600)
        if is_click_button(600, 600):
            conversation('Good Bye!!')
            menu_exit = True


    pygame.quit()               # uninitialize all pygame modules (void) - pygame Module



def char_selection():
    # FPS
    menu_exit = False
    var_FPS = 15
    ################################# Character Selection #################################
    while not menu_exit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            
        ## Menu Background
        if True:
            obj_screen.blit(main_surface, [0, 0])
        


        ############## Buttons Settings ##############
        if True:
            char_button('', 200, 300)
            if is_click_char_button(200, 300):
                character_player = character.Character(const_screenWidth, const_screenHeight)
                
                ##@@@@@@ call the tutorial
                character_player = tutorial.main(character_player)
                playbackground(character_player)
                
                mode_selection(character_player)
                
            show_image_by_coordinate(char_button_surface_2, 600, 300)


        button('Back', 400, 600)
        if is_click_button(400, 600):
            menu_exit = True





def mode_selection(character_player):
    # FPS
    menu_exit = False
    var_FPS = 15
    ################################# Mode Selection #################################
    while not menu_exit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                    

            
        ## Menu Background
        if character_player.level < 11:
            obj_screen.blit(main_surface, [0, 0])
        else:
            obj_screen.blit(main_surface_2, [0, 0])
            

        if character_player.mode_explain == False:
            conversation('Welcome to Golden Bullet!')
            conversation('In this page, you will choose what mode to do.')
            conversation('In random battle mode, you will train ',
                         'yourself to proceed the story mode.',
                         'Defeat all the enemies randomly chosen!!',)
            
            conversation('In story mode, you will be a main character ',
                         'of the episode!',
                         'Complete the mission and enjoy it!!')
            character_player.mode_explain = True

        

        ############## Buttons Settings ##############
        if True: # after char
            large_button('Random Battle Mode', 400, 200)
            if is_click_large_button(400, 200):
                ##@@@@@@ call the random battle mode
                character_player = random_battle.main(character_player)#character_player = random_battle.main(character_player)
                playbackground(character_player)
                
            large_button('Story Mode', 400, 350)
            if is_click_large_button(400, 350):
                story_selection(character_player)

        button('Lv.' + str(character_player.level), 400, 600)

        button('Quit', 680, 600)
        if is_click_button(680, 600):
            quit()


def story_selection(character_player):
    # FPS
    menu_exit = False
    var_FPS = 15
    ################################# Main Menu #################################
    while not menu_exit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                    

            
        ## Menu Background
        if character_player.level < 11:
            obj_screen.blit(main_surface, [0, 0])
        else:
            obj_screen.blit(main_surface_2, [0, 0])
        
        if character_player.story_explain == False:
            conversation('Story Mode: We have 3 episodes to proceed.',
                         '- Chapter 1: Save Illene from unstable vampires',
                         '(level 1 is required.)',
                         "- Chapter 2: Break into D.I.O's castle.",
                         '(level 6 is required.)',
                         "- Chapter 3: Defeat D.I.O.",
                         '(level 11 is required.)')
            character_player.story_explain = True
        

        ############## Buttons Settings ##############
        if True: # story line
            large_button('Mission #1: Rescue', 400, 200 - 50)
            if is_click_large_button(400, 200 - 50) and character_player.level >= 1:
                ##@@@@@@ call the story 1
                character_player = story1.main(character_player) #character_player = story1.main(character_player)
                playbackground(character_player)
                
            if character_player.level < 1:
                show_image_by_coordinate(button_lock_surface, 400, 200 - 50)
                
                
            large_button('Mission #2: Incursion', 400, 350 - 50)
            if is_click_large_button(400, 350 - 50) and character_player.level >= 6 and character_player.seen_intro_1:
                ##@@@@@@ call the story 2
                character_player = story2.main(character_player) #character_player = story2.main(character_player)
                playbackground(character_player)

            if character_player.level < 6 or not character_player.seen_intro_1:
                show_image_by_coordinate(button_lock_surface, 400, 350 - 50)

                
            large_button('Mission #3: D.I.O', 400, 500 - 50)
            if is_click_large_button(400, 500 - 50) and character_player.level >= 11 and character_player.seen_intro_2:
                ##@@@@@@ call the story 3
                character_player = story3.main(character_player) #character_player = story3.main(character_player)
                playbackground(character_player)

            if character_player.level < 11 or not character_player.seen_intro_2:
                show_image_by_coordinate(button_lock_surface, 400, 500 - 50)

        button('Lv.' + str(character_player.level), 400, 600)
        
        button('Back', 120, 600)
        if is_click_button(120, 600):
            menu_exit = True




















def is_click_char_button(x, y): # event_handler
    result = False
    
    cursur = pygame.mouse.get_pos()
    mouse_action = pygame.mouse.get_pressed()
    
    if abs(cursur[0] - x) <= char_button_w / 2 and abs(cursur[1] - y) <= char_button_h / 2 and mouse_action[0] == 1:
        result = True
    else:
        result = False
    return result


def char_button(string, x, y):
    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= char_button_w / 2 and abs(cursur[1] - y) <= char_button_h / 2:
        show_image_by_coordinate(char_button_surface_hover, x, y)
    else:
        show_image_by_coordinate(char_button_surface, x, y)

    char_button_message(string, x, y)


def char_button_message(string, x, y):
    text_surface = obj_font_georgia_small.render(string, True, pygame.Color(0, 0, 0))
    text_surface_hover = obj_font_georgia_small.render(string, True, pygame.Color(255, 255, 255))

    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= char_button_w / 2 and abs(cursur[1] - y) <= char_button_h / 2:
        show_image_by_coordinate(text_surface_hover, x, y)
    else:
        show_image_by_coordinate(text_surface, x, y)



def is_click_button(x, y): # event_handler
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




def is_click_large_button(x, y): # event_handler
    result = False
    
    cursur = pygame.mouse.get_pos()
    mouse_action = pygame.mouse.get_pressed()
    
    if abs(cursur[0] - x) <= large_button_w / 2 and abs(cursur[1] - y) <= large_button_h / 2 and mouse_action[0] == 1:
        result = True
    else:
        result = False
    return result


def large_button(string, x, y):
    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= large_button_w / 2 and abs(cursur[1] - y) <= large_button_h / 2:
        show_image_by_coordinate(large_button_surface_hover, x, y)
    else:
        show_image_by_coordinate(large_button_surface, x, y)

    large_button_message(string, x, y)


def large_button_message(string, x, y):
    text_surface = obj_font_georgia_small.render(string, True, pygame.Color(0, 0, 0))
    text_surface_hover = obj_font_georgia_small.render(string, True, pygame.Color(255, 255, 255))

    cursur = pygame.mouse.get_pos()

    if abs(cursur[0] - x) <= large_button_w / 2 and abs(cursur[1] - y) <= large_button_h / 2:
        show_image_by_coordinate(text_surface_hover, x, y)
    else:
        show_image_by_coordinate(text_surface, x, y)









def show_image_by_coordinate(image, x, y):
    image_rect = image.get_rect() # get_rect() returns a rectangle has same width and height as surface
    image_rect.center = (int(x), int(y)) # center the message!! (destination)
    obj_screen.blit(image, image_rect)







def conversation(string1='', string2='', string3='', string4='', string5='', string6='', string7='', string8=''):
    conv = True
    while conv:
        box_message(string1, 1)
        box_message(string2, 2)
        box_message(string3, 3)
        box_message(string4, 4)
        box_message(string5, 5)
        box_message(string6, 6)
        box_message(string7, 7)
        box_message(string8, 8)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    conv = False

def box_message(string, num_of_line):
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



# For images on skills and characters
def show_rect(rect):
    color1 = random.randrange(0, 255)
    color2 = random.randrange(0, 255)
    color3 = random.randrange(0, 255)
    pygame.draw.rect(obj_screen, (color1, color2, color3), rect)


    
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


    

def show_image_on_rec(image, given_x, given_y):
    x = given_x + random.randrange(-50, 51)
    y = given_y + random.randrange(-50, 51)
    rect = pygame.Rect(x, y, 200, 200)
    obj_screen.blit(image, rect)


def skill_muda(boss_object, character_player):
    play_wav_sound(const_sound_muda)

    for muda in range(13):
        show_image_on_rec(obj_image_muda_skil, boss_object.get_muda_x(), boss_object.get_muda_y())
        skill = []
        skill.append(boss_object.get_skill_muda())
        character_player.damaged_by(boss_object, skill, boss_object.get_skill_muda_damage())
        
        show_interface(character_player, character_player.level, character_player.bullet)
        pygame.display.update()
        time.sleep(0.22)

    show_image_on_rec(obj_image_muda_skil, boss_object.get_muda_x(), boss_object.get_muda_y())
    skill = []
    skill.append(boss_object.get_skill_muda())
    character_player.damaged_by(boss_object, skill, boss_object.get_skill_muda_damage())

    show_interface(character_player, character_player.level, character_player.bullet)
    pygame.display.update()
    time.sleep(0.6)



















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



def skill_a(character_player, enemy_list, illene_list, killer_list, boss_object_1):
    play_wav_sound(const_sound_skill_a) # skill a sound

    character_player.use_bullet()
    show_cylinder(character_player.bullet)
    
    show_image_by_rect_list(generate_image_list(character_player.get_skill_1_rect(), obj_image_skill_3_4, 10), character_player.get_skill_1_rect())
    
    show_interface(character_player, character_player.level, character_player.bullet)

    
    for x in range(len(enemy_list)):
        enemy_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    for x in range(len(illene_list)):
        illene_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    for x in range(len(killer_list)):
        killer_list[x].damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())
    boss_object_1.damaged_by(character_player, character_player.get_skill_1_rect(), character_player.get_skill_1_damage())


    
    pygame.display.update()
    time.sleep(character_player.get_a_delay())  # skill a delay




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


def playbackground(character_player):
    if character_player.level >= 11:
        bgm = const_music_main_theme_2
    else:
        bgm = const_music_main_theme
    pygame.mixer.music.load(bgm)
    pygame.mixer.music.set_volume(0.35)
    pygame.mixer.music.play(-1)


main_menu()
