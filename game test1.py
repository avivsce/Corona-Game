import pygame, sys
import random
import time

pygame.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clock = pygame.time.Clock()
display_width, display_height = 1080, 920
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(white)
balls = []


class Circle():
    def __init__(self, x_cord, y_cord, x_vel, y_vel):
        self.player_surface = screen
        self.player_color = blue
        self.player_radius = 10
        self.player_pos_x = x_cord
        self.player_pos_y = y_cord
        self.speed_x = x_vel
        self.speed_y = y_vel

    def draw(self):
        pygame.draw.circle(screen, self.player_color, (self.player_pos_x, self.player_pos_y), self.player_radius)

    def update(self):
        self.player_pos_x -= self.speed_x
        self.player_pos_y += self.speed_y

    def bouncing_rect(self):
        if self.player_pos_x < 100:
            self.speed_x *= -1
        if self.player_pos_x > 1000:
            self.speed_x *= -1
        if self.player_pos_y < 10:
            self.speed_y *= -1
        if self.player_pos_y > 900:
            self.speed_y *= -1
def colide(array_balls):
    for i in range(len(array_balls)):
        for j in range(i+1,(len(array_balls))):
            if abs(array_balls[i].player_pos_x - array_balls[j].player_pos_x) < 13 and abs(array_balls[i].player_pos_y - array_balls[j].player_pos_y) < 13:
                array_balls[i].speed_x *= -1
                array_balls[i].speed_y *= -1
                array_balls[j].speed_x *= -1
                array_balls[j].speed_y *= -1
                if array_balls[i].player_color == red and array_balls[j].player_color == blue:
                    array_balls[j].player_color = red
                if array_balls[i].player_color == blue and array_balls[j].player_color == red:
                    array_balls[i].player_color = red
                print("im tired of this shit ")


def game():
    balls.append(Circle(random.uniform(150, 600), random.uniform(50, 850), 3, 3))
    balls[0].player_color = red
    for i in range(20):
        balls.append(Circle(random.uniform(150, 800), random.uniform(50, 850), 3, 3))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(white)
        colide(balls)
        [Circle.bouncing_rect() for Circle in balls]
        [Circle.update() for Circle in balls]
        [Circle.draw() for Circle in balls]
        pygame.display.update()
        clock.tick(60)


game()
pygame.quit()
