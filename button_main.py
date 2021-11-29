import pygame
import button

# create display window
SCREEN_WEIGHT = 500
SCREE_WIDTH = 800

screen = pygame.display.set_mode((SCREE_WIDTH, SCREEN_WEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
start_img = pygame.image.load('play.png.jpg').convert_alpha()
exit_img = pygame.image.load('quit.png.jpg').convert_alpha()

# create button instances
start_button = button.Button(300, 150, start_img, 0.8)
exit_button = button.Button(300, 250, exit_img, 0.8)

# game loop
run = True
while run:
    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        run = False

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()