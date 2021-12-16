import pygame
import pymunk
import random
pygame.init()

FPS =60
BK_color = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
height,width = 1000,700

screen = pygame.display.set_mode((height,width)) #create screen
clock = pygame.time.Clock()
space = pymunk.Space()
pygame.display.set_caption('corona game') #game title


###################################
def convert_coordinates(point):
    return int(point[0]), 600-int(point[1])
ball_radius = 10
class Ball():
    def __init__(self,x,y,collision_type, up = 1):
        self.body = pymunk.Body()
        self.body.position = x,y
        self.body.velocity = random.uniform( -100,100),random.uniform(-100,100)
        self.shape = pymunk.Circle(self.body,ball_radius)
        self.shape.elasticity = 1
        self.shape.density = 1
        self.shape.collision_type = collision_type
        space.add(self.body,self.shape)

    def draw(self):
        if self.shape.collision_type != 2:
            pygame.draw.circle(screen, blue, convert_coordinates(self.body.position), 10)
        else:
            pygame.draw.circle(screen, red, convert_coordinates(self.body.position), 10)

    def change_to_red(self,arbiter, space, data):
        self.shape.collision_type = 2


    def check_boarder():
        for i in range(100):
            if balls[i].x < 700:
                 balls[i].velocity *= -1

class Floor():
    def __init__(self):
        self.body = pymunk.Body (body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body,(0, 0), (600, 50), 5)
        self.shape.elasticity = 1
        space.add(self.body,self.shape)

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (250, 0), (1000, 0), 10)
        pygame.draw.line(screen, (0, 0, 0), (250, 0), (250, 700), 10)
        pygame.draw.line(screen, (0, 0, 0), (250, 700), (1000, 700), 10)
        pygame.draw.line(screen, (0, 0, 0), (1000, 0), (1000, 700), 10)


###################################
#pygame.display.flip()

def game():

    balls = [Ball(random.randint(600,900), random.randint(150,650),i+3) for i in range (100)]
    balls.append(Ball(400,400,2))
    floor = Floor()
    handlers = [space.add_collision_handler(2,i+3) for i in range (100)]
    for i, handler in enumerate(handlers):
        handler.separate = balls[i].change_to_red


    for i in range(100):
        handler.separate = balls[i].check_boarder



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BK_color)  # screen color
        [ball.draw() for ball in balls]
        floor.draw()
        pygame.display.update()
        clock.tick(FPS)
        space.step(1/FPS)
game()
pygame.quit()

