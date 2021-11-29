import pygame, sys
blue =(0, 0, 255)
red = (255, 0, 0)
white = (255, 255,255)
FPS = 60
width,height = 800,700
def bouncing_rect():
    global r_x_speed, r_y_speed, b_x_speed,b_y_speed,flag
    red_rect.x += r_x_speed
    red_rect.y += r_y_speed
    blue_rect.x += b_x_speed
    blue_rect.y += b_y_speed


    # collision with boarder
    if red_rect.right>= screen_width or red_rect.left <=0:
        r_x_speed *=-1
    if red_rect.bottom>= screen_height or red_rect.top <=0:
        r_y_speed *=-1
    if blue_rect.right>= screen_width or blue_rect.left <=0:
        b_x_speed *=-1
    if blue_rect.bottom>= screen_height or blue_rect.top <=0:
        b_y_speed *=-1
    collision_tolerance = 10
    if red_rect.colliderect(blue_rect):
        flag = False
        if abs(red_rect.top == blue_rect.bottom) < collision_tolerance:
            r_y_speed *= -1
            b_y_speed *= -1
        if abs(red_rect.left - blue_rect.right) < collision_tolerance:
            r_x_speed *= -1
            b_x_speed *= -1


    if(flag):
        pygame.draw.rect(screen,blue, blue_rect)
    else:
        pygame.draw.rect(screen, red, blue_rect)
    pygame.draw.rect(screen, red, red_rect)

pygame.init()
clock = pygame.time.Clock()
screen_width,screen_height = width, height
screen = pygame.display.set_mode((screen_width,screen_height))
flag = True
red_rect = pygame.Rect(350,350,100,100)
r_x_speed, r_y_speed = -5,4

blue_rect = pygame.Rect(300,500,100,100)
b_x_speed, b_y_speed = 3,2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    bouncing_rect()
    pygame.display.flip()
    clock.tick(FPS)
