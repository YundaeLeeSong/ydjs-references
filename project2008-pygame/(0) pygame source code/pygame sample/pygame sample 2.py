import pygame               # all available pygame submodules are automatically imported. - pygame Module
import math
import random
import time

pygame.init()               # initialize all imported pygame modules (return: tuple). - pygame Module


# data set for computer player!
tuple_movement = ((2, 0), (-2, 0), (0, 2), (0, -2),
                  (1.414, 1.414), (-1.414, 1.414),
                  (-1.414, -1.414), (1.414, -1.414),
                  (0, 0))


# constants
const_music_background_1 = r'sounds\background_1.mp3'
const_music_background_2 = r'sounds\background_2.mp3'
const_music_background_3 = r'sounds\background_3.mp3'
const_music_boss = r'sounds\boss.mp3'
const_music_main_theme = r'sounds\main_theme.mp3'
const_music_skill_a = r'sounds\skill_1.wav'
const_music_skill_s = r'sounds\skill_2.wav'
const_music_skill_d = r'sounds\skill_3.wav'
const_music_skill_f = r'sounds\skill_4.wav'
const_music_story_1 = r'sounds\story_1.mp3'
const_music_story_2 = r'sounds\story_2.mp3'


const_screenWidth = 800
const_screenHeight = 600

const_playerWidth = 30 ##
const_playerHeight = 40 ##
var_range = 30 ##

const_skill_blockSize = 10 ## 
const_move_straight = 2 ##
const_move_diagonal = const_move_straight / math.sqrt(2) ## 

# screen
obj_screen = pygame.display.set_mode((const_screenWidth, const_screenHeight)) # return a screen object (return: screen object) - pygame.display Module
pygame.display.set_caption('Sample Game')

# objects
obj_clock = pygame.time.Clock() # return a clock object (return: clock object) - pygame.time Module

def gameLoop():
    # Background Music
    play_background_music(const_music_main_theme)
    
    # Variables and Objects
    var_gameExit = False
    is_skill_a_use = False ##
    is_skill_s_use = False ## 
    is_skill_d_use = False ##
    is_skill_f_use = False ## 
    
    var_xPosition = const_screenWidth / 2 ##
    var_yPosition = const_screenHeight / 2 ##
    var_changeX = 0 ##
    var_changeY = 0 ##
    var_directionX = 0 ##
    var_directionY = const_move_straight ##

    var_skill_a_delay = 0.2 ##
    var_skill_s_1_delay = 1.2 ##
    var_skill_s_2_delay = 0.5 ##
    var_skill_d_delay = 1.8 ##
    var_skill_f_delay = 1.2 ##

    var_FPS = 120

    obj_rect_player = pygame.Rect(int(var_xPosition), int(var_yPosition), const_playerWidth, const_playerHeight) ## 
    # obj_rect_skill_1 = get_skill_1(obj_rect, (var_changeX, var_changeY, var_directionX, var_directionY), var_range) ##
    # obj_rect_skill_2 = get_skill_2(obj_rect, (var_changeX, var_changeY, var_directionX, var_directionY), var_range) ## 
    # obj_rect_skill_3 = get_skill_3(obj_rect, (var_changeX, var_changeY, var_directionX, var_directionY), var_range) ##

    ## start!!
    while not var_gameExit:
        pygame.display.update()     # update the screen (void) - pygame.display Module
        obj_clock.tick(var_FPS)     # set frames per second
        
        ## keyboard input (INPUT)
        for obj_event in pygame.event.get():
            # exit
            if obj_event.type == pygame.QUIT:       
                var_gameExit = True
                
            # keydown
            if obj_event.type == pygame.KEYDOWN:
                if obj_event.key == pygame.K_LEFT:
                    var_changeX = -const_move_straight
                if obj_event.key == pygame.K_RIGHT:
                    var_changeX = const_move_straight
                if obj_event.key == pygame.K_UP:
                    var_changeY = -const_move_straight
                if obj_event.key == pygame.K_DOWN:
                    var_changeY = const_move_straight
                if obj_event.key == pygame.K_a:
                    is_skill_a_use = True
                if obj_event.key == pygame.K_s:
                    is_skill_s_use = True
                if obj_event.key == pygame.K_d:
                    is_skill_d_use = True
                if obj_event.key == pygame.K_f:
                    is_skill_f_use = True
                if obj_event.key == pygame.K_SPACE:
                    var_FPS = 240
                    
            # keyup
            if obj_event.type == pygame.KEYUP:
                if obj_event.key == pygame.K_LEFT or obj_event.key == pygame.K_RIGHT:
                    var_changeX = 0
                if obj_event.key == pygame.K_UP or obj_event.key == pygame.K_DOWN:
                    var_changeY = 0
                if obj_event.key == pygame.K_a:
                    is_skill_a_use = False
                if obj_event.key == pygame.K_s:
                    is_skill_s_use = False
                if obj_event.key == pygame.K_d:
                    is_skill_d_use = False
                if obj_event.key == pygame.K_f:
                    is_skill_f_use = False
                if obj_event.key == pygame.K_SPACE:
                    var_FPS = 120

                    
        ## Action Settings (PROCESS) ##
        # keyinput_validation
        var_changeX, var_changeY = keyinput_validation(var_changeX, var_changeY)
        # set up direction
        var_directionX, var_directionY = get_direction(var_directionX, var_directionY, var_changeX, var_changeY)
        # Movement
        var_xPosition, var_yPosition = set_location(var_xPosition, var_yPosition, var_changeX, var_changeY)
        # update the player location
        obj_rect_player = pygame.Rect(int(var_xPosition), int(var_yPosition), const_playerWidth, const_playerHeight)



        ## Display results (OUTPUT)
        # screen - background color
        obj_screen.fill((255, 255, 255))            # fill method of screen object sets the background color (arg: tuple, void) - pygame.display Module
        # screen - draw player
        pygame.draw.rect(obj_screen, (0, 0, 0), obj_rect_player)
        # screen - skill use
        if is_skill_a_use:
            play_wav_sound(const_music_skill_a) # skill a sound
            
            show_skill(get_skill_1(obj_rect_player, (var_changeX, var_changeY, var_directionX, var_directionY), var_range))
            time.sleep(var_skill_a_delay)  # skill a delay
            
        if is_skill_s_use:
            play_wav_sound(const_music_skill_s) # skill s sound
            
            show_skill(get_skill_1(obj_rect_player, (var_changeX, var_changeY, var_directionX, var_directionY), var_range))
            time.sleep(var_skill_s_1_delay)  # skill s delay
            show_skill(get_skill_2(obj_rect_player, (var_changeX, var_changeY, var_directionX, var_directionY), var_range))
            time.sleep(var_skill_s_2_delay)  # skill s delay

        if is_skill_d_use:
            play_wav_sound(const_music_skill_d) # skill d sound
            
            show_skill(get_skill_2(obj_rect_player, (var_changeX, var_changeY, var_directionX, var_directionY), var_range))
            time.sleep(var_skill_d_delay) # skill d delay

        if is_skill_f_use:
            play_wav_sound(const_music_skill_f) # skill f sound
            
            show_skill(get_skill_3(obj_rect_player, (var_changeX, var_changeY, var_directionX, var_directionY), var_range))
            time.sleep(var_skill_f_delay) # skill f delay
        
        
    pygame.quit()               # uninitialize all pygame modules (void) - pygame Module
    quit()

def play_background_music(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def play_wav_sound(filename):
    sound = pygame.mixer.Sound(filename)
    sound.set_volume(1)
    sound.play()

def set_location(x, y, dx, dy):
    x += dx
    y += dy
    if (x > const_screenWidth - const_playerWidth or x < 0
        or
        y > const_screenHeight - const_playerHeight or y < 0):
        x -= dx
        y -= dy
    return x, y

def get_direction(x_direction, y_direction, dx, dy):
    if not (dx == 0 and dy == 0):
        a = dx
        b = dy
    else:
        a = x_direction
        b = y_direction
    return a, b

def keyinput_validation(var_changeX, var_changeY):
    if abs(math.sqrt(var_changeX ** 2 + var_changeY ** 2) - const_move_straight) > 0.01:
        if var_changeX * var_changeY != 0:
            var_changeX = var_changeX / abs(var_changeX) * math.sqrt(2)
            var_changeY = var_changeY / abs(var_changeY) * math.sqrt(2)
        if var_changeX == 0 and var_changeY < 0:
            var_changeY = -const_move_straight
        if var_changeX == 0 and var_changeY > 0:
            var_changeY = const_move_straight
        if var_changeY == 0 and var_changeX < 0:
            var_changeX = -const_move_straight
        if var_changeY == 0 and var_changeX > 0:
            var_changeX = const_move_straight
    return var_changeX, var_changeY

def get_skill_3(player_rect, direction_list, skill_len):
    list_of_rectangles = []
    x = player_rect.x
    y = player_rect.y
    w = player_rect.w
    h = player_rect.h
    if direction_list[2] == 0:
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 12, y, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect3 = get_skill_1(pygame.Rect(x - 12, y, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect4 = get_skill_1(pygame.Rect(x + 24, y, w ,h), direction_list, skill_len, 20)
        rect5 = get_skill_1(pygame.Rect(x - 24, y, w ,h), direction_list, skill_len, 20)
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
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x, y + 12, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect3 = get_skill_1(pygame.Rect(x, y - 12, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect4 = get_skill_1(pygame.Rect(x, y + 24, w ,h), direction_list, skill_len, 20)
        rect5 = get_skill_1(pygame.Rect(x, y - 24, w ,h), direction_list, skill_len, 20)
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
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 8, y - 8, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect3 = get_skill_1(pygame.Rect(x - 8, y + 8, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect4 = get_skill_1(pygame.Rect(x + 16, y - 16, w ,h), direction_list, skill_len, 20)
        rect5 = get_skill_1(pygame.Rect(x - 16, y + 16, w ,h), direction_list, skill_len, 20)
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
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 8, y + 8, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect3 = get_skill_1(pygame.Rect(x - 8, y - 8, w ,h), direction_list, int(skill_len * 1.2), 15)
        rect4 = get_skill_1(pygame.Rect(x + 16, y + 16, w ,h), direction_list, skill_len, 20)
        rect5 = get_skill_1(pygame.Rect(x - 16, y - 16, w ,h), direction_list, skill_len, 20)
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

def get_skill_2(player_rect, direction_list, skill_len):
    list_of_rectangles = []
    x = player_rect.x
    y = player_rect.y
    w = player_rect.w
    h = player_rect.h
    if direction_list[2] == 0:
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 12, y, w ,h), direction_list, skill_len, 10)
        rect3 = get_skill_1(pygame.Rect(x - 12, y, w ,h), direction_list, skill_len, 10)
        for x in rect1:
            list_of_rectangles.append(x)
        for x in rect2:
            list_of_rectangles.append(x)
        for x in rect3:
            list_of_rectangles.append(x)
    elif direction_list[3] == 0:
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x, y + 12, w ,h), direction_list, skill_len, 10)
        rect3 = get_skill_1(pygame.Rect(x, y - 12, w ,h), direction_list, skill_len, 10)
        for x in rect1:
            list_of_rectangles.append(x)
        for x in rect2:
            list_of_rectangles.append(x)
        for x in rect3:
            list_of_rectangles.append(x)
    elif direction_list[2] * direction_list[3] > 0:
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 8, y - 8, w ,h), direction_list, skill_len, 10)
        rect3 = get_skill_1(pygame.Rect(x - 8, y + 8, w ,h), direction_list, skill_len, 10)
        for x in rect1:
            list_of_rectangles.append(x)
        for x in rect2:
            list_of_rectangles.append(x)
        for x in rect3:
            list_of_rectangles.append(x)
    elif direction_list[2] * direction_list[3] < 0:
        rect1 = get_skill_1(pygame.Rect(x, y, w ,h), direction_list, int(skill_len * 1.5))
        rect2 = get_skill_1(pygame.Rect(x + 8, y + 8, w ,h), direction_list, skill_len, 10)
        rect3 = get_skill_1(pygame.Rect(x - 8, y - 8, w ,h), direction_list, skill_len, 10)
        for x in rect1:
            list_of_rectangles.append(x)
        for x in rect2:
            list_of_rectangles.append(x)
        for x in rect3:
            list_of_rectangles.append(x)
        
    return list_of_rectangles
    
    

def get_skill_1(player_rect, direction_list, skill_len, start_len=3):
    list_of_rectangles = []
    if direction_list[0] == 0 and direction_list[1] == 0:
        for x in range(start_len, int(skill_len) + start_len):
            obj_rect = pygame.Rect(int(player_rect.centerx - const_skill_blockSize / 2 + 5 * x * direction_list[2]),
                                   int(player_rect.centery - const_skill_blockSize / 2 + 5 * x * direction_list[3]),
                                   const_skill_blockSize,
                                   const_skill_blockSize)
            list_of_rectangles.append(obj_rect)
    else:
        for x in range(start_len, int(skill_len) + start_len):
            obj_rect = pygame.Rect(int(player_rect.centerx - const_skill_blockSize / 2 + 5 * x * direction_list[0]),
                                   int(player_rect.centery - const_skill_blockSize / 2 + 5 * x * direction_list[1]),
                                   const_skill_blockSize,
                                   const_skill_blockSize)
            list_of_rectangles.append(obj_rect)
    return list_of_rectangles
        
def show_skill(rect_list):
    for x in range(len(rect_list)):
        pygame.draw.rect(obj_screen, (x * 0.2 + 100, x * 0.2 + 100, 100), rect_list[x])
    pygame.display.update()
    

gameLoop()
