import pygame               # all available pygame submodules are automatically imported. - pygame Module
import time
import random

pygame.init()               # initialize all imported pygame modules (return: tuple). - pygame Module

# constants
const_screenWidth = 800
const_screenHeight = 600
const_icon_name = r'pictures\icon.png'
const_blockSize = 10
const_FPS = 120

# background constants ################################
const_background_size_x = 3 
const_background_size_y = 2
const_random_list = [] 
for x in range(const_background_size_x * const_background_size_y):
    const_random_list.append(random.randrange(0, 4))

# screen
obj_screen = pygame.display.set_mode((const_screenWidth, const_screenHeight)) # return a screen object (return: screen object) - pygame.display Module
pygame.display.set_caption('Sample Game')     # set the caption of the screen (void) -  pygame.display Module
obj_image_icon = pygame.image.load(const_icon_name).convert_alpha()
pygame.display.set_icon(obj_image_icon)


# objects
obj_clock = pygame.time.Clock() # return a clock object (return: clock object) - pygame.time Module
obj_font = pygame.font.SysFont(None, 25) # return a font object (arg1: str, arg2: int, return: font object) - pygame.font Module

obj_image_1 = pygame.image.load(r'pictures\background_1_1.png').convert()
obj_image_2 = pygame.image.load(r'pictures\background_1_2.png').convert()
obj_image_3 = pygame.image.load(r'pictures\background_1_3.png').convert()

def gameLoop():
    # Variables
    var_gameExit = False
    var_gameOver = False
    
    var_xPosition = const_screenWidth / 2
    var_yPosition = const_screenHeight / 2
    var_changeX = 0
    var_changeY = 0

    x = 0 ###
    y = 0 ###
    dx = 0 ###
    dy = 0 ###
    


    var_randAppleX = random.randrange(0, const_screenWidth - const_blockSize) // 2 * 2
    var_randAppleY = random.randrange(0, const_screenHeight - const_blockSize) // 2 * 2

    
    while not var_gameExit:
        # Gameover
        if var_xPosition == 100:
            var_gameOver = True
        
        while var_gameOver == True:
            message_to_screen('Game over, press C to play again or Q to quit', (255, 0, 0))
            pygame.display.update()

            for obj_event in pygame.event.get():
                if obj_event.type == pygame.KEYDOWN:
                    if obj_event.key == pygame.K_q:
                        var_gameOver = False
                        var_gameExit = True
                    if obj_event.key == pygame.K_c:
                        gameLoop()

        
        # keyboard input
        for obj_event in pygame.event.get():        # get the event obejct (return: event object) - pygame.event Module
            
            if obj_event.type == pygame.QUIT:       # constant for quit (x on the right top of the window) - pygame Module
                var_gameExit = True
                
            if obj_event.type == pygame.KEYDOWN:    # constant for keydown (press a button) - pygame Module
                if obj_event.key == pygame.K_LEFT:  # constant for left key - pygame Module
                    dx = 2
                if obj_event.key == pygame.K_RIGHT: # constant for right key - pygame Module
                    dx = -2
                if obj_event.key == pygame.K_UP:    # constant for up key - pygame Module
                    dy = 2
                if obj_event.key == pygame.K_DOWN:  # constant for down key - pygame Module
                    dy = -2
                    
            if obj_event.type == pygame.KEYUP:      # constant for keyup (release a button) - pygame Module
                if obj_event.key == pygame.K_LEFT or obj_event.key == pygame.K_RIGHT:
                    dx = 0
                if obj_event.key == pygame.K_UP or obj_event.key == pygame.K_DOWN:
                    dy = 0
        # movement
        x, y = set_background(x, y, dx, dy)
        show_background(x, y)




        # screen - draw
        pygame.draw.rect(obj_screen, (255, 0, 0), [var_randAppleX, var_randAppleY, const_blockSize, const_blockSize])
        pygame.draw.rect(obj_screen, (0, 0, 0), [int(var_xPosition), int(var_yPosition), const_blockSize, const_blockSize]) # draw a rectangle (arg1: screen object, arg2: color, arg3: list, void)

        # set up background
        

        # action
        if abs(var_randAppleX - var_xPosition) < const_blockSize and abs(var_randAppleY - var_yPosition) < const_blockSize:
            var_randAppleX = random.randrange(0, const_screenWidth - const_blockSize) // 2 * 2
            var_randAppleY = random.randrange(0, const_screenHeight - const_blockSize) // 2 * 2

        pygame.display.update()     # update the screen (void) - pygame.display Module

        # clock - tick
        obj_clock.tick(const_FPS)                         # tick method of clock object sets the frames per second (arg: int, void) - pygame.time Module


    message_to_screen('Exit the game...', (255, 0, 0))
    pygame.display.update()
    time.sleep(1)
    
    pygame.quit()               # uninitialize all pygame modules (void) - pygame Module
    quit()


def message_to_screen(msg, color):
    screen_text = obj_font.render(msg, True, color)
    obj_screen.blit(screen_text, [int(const_screenWidth / 2), int(const_screenHeight / 2)])

def set_background(x, y, dx, dy):
    x += dx
    y += dy
    if (-const_screenWidth * (const_background_size_x - 1) + x > 0
        or x < 0):
        x -= dx
    if (-const_screenHeight * (const_background_size_y - 1) + y > 0
        or y < 0):
        y -= dy
    return x, y

def show_background(x, y):
    counter = 0
    for n_x in range(const_background_size_x):
        for n_y in range(const_background_size_y):
            if const_random_list[counter] <= 1:
                obj_screen.blit(obj_image_1,
                                [-const_screenWidth * (n_x) + x,
                                 -const_screenHeight * (n_y) + y])
            if const_random_list[counter] == 2:
                obj_screen.blit(obj_image_2,
                                [-const_screenWidth * (n_x) + x,
                                 -const_screenHeight * (n_y) + y])
            if const_random_list[counter] == 3:
                obj_screen.blit(obj_image_3,
                                [-const_screenWidth * (n_x) + x,
                                 -const_screenHeight * (n_y) + y])
            counter += 1

gameLoop()
