import pygame, sys
import random

pygame.init()
# colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
sw = 800
sh = 600


gameWindow = pygame.display.set_mode((sw, sh))
pygame.display.set_caption('snake game')
pygame.display.update()

score = 0
snake_x = 50
snake_y = 45
snake_size = 10
food_x = random.randint(20, sw / 2)
food_y = random.randint(20, sh / 2)
velocity_x = 0
velocity_y = 0
snake_head = 0
init_velocity = 5
exit_game = False
gameover : bool = False
fps = 60

clock = pygame.time.Clock()

snk_list = []
snk_length = 1

def snake_loop (gameWindo, color , snk_list , snake_size ):
    for x,y in snk_list:
        pygame.draw.rect(gameWindo, color,[x,y,snake_size,snake_size])
font = pygame.font.SysFont(None,55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])




while not exit_game:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            elif event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0
            elif event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0
    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
        score += 10
        snk_length += 5



        food_x = random.randint(20, sw / 2)
        food_y = random.randint(20, sh / 2)


    gameWindow.fill(white)
    text_screen("Score :"+str(score),red,600,30)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    if len(snk_list) > snk_length:
        del snk_list[0]


    snake_loop(gameWindow,black,snk_list,snake_size)


    if head in snk_list[:-1] :
        gameover = True
    if snake_x>sw or snake_x<0 or snake_y<0 or snake_y>sh:
        gameover=True

    if gameover == True:
        gameWindow.fill(white)
        text_screen("game over ",red, 100 ,250 )



    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()