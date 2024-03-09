import pygame
import time
import random
snake_speed = 12
# Window size
window_x = 720
window_y = 480
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color((255,255,255))
blue = pygame.Color((0,0,255))
green = pygame.Color((0,255,0))
red = pygame.Color((255,0,0))
black = pygame.Color((0,0,0))
orange = pygame.Color((255,100,10))
yellow = pygame.Color((255,255,0))
blue_green = pygame.Color((0,255,170))
marroon = pygame.Color((115,0,0))
lime = pygame.Color((180,255,100))
pink = pygame.Color((255,100,180))
purple = pygame.Color((240,0,255))
gray = pygame.Color((127,127,127))
magenta = pygame.Color((255,0,230))
brown = pygame.Color((100,40,0))
forest_green = pygame.Color((0,50,0))
navy_blue = pygame.Color((0,0,100))
rust = pygame.Color((210,150,75))
dandilion_yellow = pygame.Color((255,200,0))
highlighter = pygame.Color((255,255,100))
sky_blue = pygame.Color((0,255,255))
light_gray = pygame.Color((200,200,200))
dark_gray = pygame.Color((50,50,50))
tan = pygame.Color((230,220,170))
coffee_brown = pygame.Color((200,190,140))
moon_glow = pygame.Color((235,245,255))
# Initialising pygame
pygame.init()
# Initialise game window
pygame.display.set_caption('Sudhanshu Singh Snakes Game')
game_window = pygame.display.set_mode((window_x, window_y))
# FPS (frames per second) controller
fps = pygame.time.Clock()
# sound when snake eats the fruit
eating_sound = pygame.mixer.Sound('sound_eating.wav')
#sound when game over as snake collide with the wall
game_over_sound = pygame.mixer.Sound('game_over_sound.wav')
# background music during the game
music = pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(-1)
# defining snake default position
snake_position = [100, 90]
# defining first 4 blocks of snake
# body
snake_body = [ [100, 90],
 [90, 90],
 [80, 90],
 [70, 90]
 ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
 random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
# setting default snake direction
# towards right
direction = 'DOWN'
change_to = direction
# initial score
score = 0
hscore = 0
gameover = False
# displaying Score function
def show_score(choice, color, font, size):
 
 # creating font object score_font
 score_font = pygame.font.SysFont(font, size)
 high_font=pygame.font.SysFont('times new roman',20,bold=True)
 # create the display surface object
 # score_surface
 score_surface = score_font.render('Score : ' + str(score), True, color)
 high_surface=high_font.render('High Score : '+ str(hscore),True,white)
 
 # create a rectangular object for the
 # text surface object
 score_rect = score_surface.get_rect()
 high_rect=high_surface.get_rect()
 high_rect.topleft=(0,20)
 # displaying text
 game_window.blit(score_surface, score_rect)
 game_window.blit(high_surface,high_rect)
 # game over function
def game_over(): 
 
 # creating font object my_font
 my_font = pygame.font.SysFont('algerian', 60)
 my_fonths= pygame.font.SysFont('times new roman', 30)
 # creating a text surface on which text
 # will be drawn
 game_over_surface = my_font.render('Your Score is : ' + str(score), True, 
orange)
 game_over_high=my_fonths.render(
'HighScore is : '+str(hscore),True,white)
 # create a rectangular object for the text
 # surface object
 game_over_rect = game_over_surface.get_rect()
 gamehigh=game_over_high.get_rect()
 # setting position of the text
 game_over_rect.midtop = (window_x/2, window_y/4)
 gamehigh.midbottom = (window_x/2, window_y/2)
 # game over sound
 game_over_sound.play() 
 # blit will draw the text on screen
 game_window.blit(game_over_surface, game_over_rect)
 pygame.display.flip()
 
 # after 2 seconds we will quit the
 # program
 time.sleep(2)
 
 # deactivating pygame library
 pygame.quit()
 
 # quit the program
 quit()
 # Main Function
while True:
 
 # handling key events
 for event in pygame.event.get():
if event.type == pygame.KEYDOWN:
if event.key == pygame.K_UP:
 change_to = 'UP'
 if event.key == pygame.K_DOWN:
 change_to = 'DOWN'
 if event.key == pygame.K_LEFT:
 change_to = 'LEFT'
 if event.key == pygame.K_RIGHT:
 change_to = 'RIGHT'
 # If two keys pressed simultaneously
 # we don't want snake to move into two directions
 # simultaneously
 if change_to == 'UP' and direction != 'DOWN':
 direction = 'UP'
 if change_to == 'DOWN' and direction != 'UP':
 direction = 'DOWN'
 if change_to == 'LEFT' and direction != 'RIGHT':
 direction = 'LEFT'
 if change_to == 'RIGHT' and direction != 'LEFT':
 direction = 'RIGHT'
 # Moving the snake
 if direction == 'UP':
 snake_position[1] -= 10
 if direction == 'DOWN':
 snake_position[1] += 10
 if direction == 'LEFT':
 snake_position[0] -= 10
 if direction == 'RIGHT':
 snake_position[0] += 10
 # Snake body growing mechanism
 # if fruits and snakes collide then scores will be
 # incremented by 10
 snake_body.insert(0, list(snake_position))
 if snake_position[0] == fruit_position[0] and snake_position[1] == 
fruit_position[1]:
 score += 10
 eating_sound.play() #sound when snake eats the fruit
 fruit_spawn = False
 else:
 snake_body.pop()
 
 if not fruit_spawn:
 fruit_position = [random.randrange(1, (window_x//10)) * 10,
 random.randrange(1, (window_y//10)) * 10]
 
 fruit_spawn = True
 game_window.fill(black)
 
 
 for pos in snake_body:
 pygame.draw.rect(game_window, sky_blue, pygame.Rect(
 pos[0], pos[1], 10, 10))
 
 pygame.draw.rect(game_window, yellow, pygame.Rect(
 fruit_position[0], fruit_position[1], 10, 10))
 # Game Over conditions
 if snake_position[0] < 0 or snake_position[0] > window_x-10:
 game_over()
 if snake_position[1] < 0 or snake_position[1] > window_y-10:
 game_over()
 
 # Touching the snake body
 for block in snake_body[1:]:
 if snake_position[0] == block[0] and snake_position[1] == block[1]:
 game_over()
 
 # displaying score continuously
 show_score(1, blue, 'roboto', 30)
 
 # Refresh game screen
 pygame.display.update()
 # Frame Per Second /Refresh Rate
 fps.tick(snake_speed)