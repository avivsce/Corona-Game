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
yellow = (255,255,0)
corona = (150, 0, 0)
healer = (0, 255, 255)
clock = pygame.time.Clock()
display_width, display_height = 1300, 800
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Statistician game")
screen.fill(white)
balls = []
mouseClick_x = 0
mouseClick_y = 0
points = 0
totalClicks = 0
mouseHit = 0
stopflag = True
stopcounter = 0
blueCount = 0
temp = 0

my_font = pygame.font.SysFont("Arial", 20)
my_font_GO = pygame.font.SysFont("Arial", 40)

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
        global stopflag
        global stopcounter
        if stopflag:
            self.player_pos_x -= self.speed_x
            self.player_pos_y += self.speed_y
            return
        if stopcounter < 1300 * 6:
            stopcounter += 1
            return
        stopcounter = 0
        stopflag = True
        return

    def bouncing_rect(self):
        if self.player_pos_x < 10:
            self.speed_x *= -1
        if self.player_pos_x > 1200:
            self.speed_x *= -1
        if self.player_pos_y < 10:
            self.speed_y *= -1
        if self.player_pos_y > 789:
            self.speed_y *= -1

def bomb(balls):
    global points
    r = 100 #r= radius
    x, y = random.randint(100, 1100), random.randint(100, 689)
    if points >= 10:
        points-=10
        pygame.draw.line(screen, yellow, (x - r, y + r), (x + r, y + r), 5)
        pygame.draw.line(screen, yellow, (x - r, y + r), (x - r, y - r), 5)
        pygame.draw.line(screen, yellow, (x + r, y + r), (x + r, y - r), 5)
        pygame.draw.line(screen, yellow, (x - r, y - r), (x + r, y - r), 5)
        pygame.display.flip()
        pygame.time.delay(100)
        for i in range(len(balls)):
            if x-r < balls[i].player_pos_x < x+r and y-r < balls[i].player_pos_y < y+r:
                if balls[i].player_color == red:
                    balls[i].player_color = blue
                    points += 1

def colide(array_balls):
    global blueCount
    for i in range(len(array_balls)):
        for j in range(i + 1, (len(array_balls))):
            if abs(array_balls[i].player_pos_x - array_balls[j].player_pos_x) < 30 and abs(
                    array_balls[i].player_pos_y - array_balls[j].player_pos_y) < 30:
                array_balls[i].speed_x *= -1
                array_balls[i].speed_y *= -1
                array_balls[j].speed_x *= -1
                array_balls[j].speed_y *= -1
                if array_balls[i].player_color == red and array_balls[j].player_color == blue:
                    array_balls[j].player_color = red
                if array_balls[i].player_color == blue and array_balls[j].player_color == red:
                    array_balls[i].player_color = red
                if array_balls[i].player_color == healer and array_balls[j].player_color == red:
                    array_balls[j].player_color = blue
                    blueCount += 1
                if array_balls[i].player_color == red and array_balls[j].player_color == healer:
                    array_balls[i].player_color = blue
                if array_balls[i].player_color == corona and array_balls[j].player_color == blue:
                    array_balls[j].player_color = red
                if array_balls[i].player_color == blue and array_balls[j].player_color == corona:
                    array_balls[i].player_color = red

def mousecheck(array_balls):
    global mouseClick_x
    global mouseClick_y
    global points
    global mouseHit
    global totalClicks
    global blueCount
    global temp
    mouseClick_x, mouseClick_y = pygame.mouse.get_pos()
    for i in range(len(array_balls)):
        if abs(array_balls[i].player_pos_x - mouseClick_x) < 30 and abs(array_balls[i].player_pos_y - mouseClick_y) < 30:
            if array_balls[i].player_color == red:
                array_balls[i].player_color = blue
                points += 1
                blueCount += 1
                print(points)
                mouseHit += 1
    totalClicks += 1
    temp = ((mouseHit/totalClicks)*100)
    print("accurecy : " + str(temp))

def endgame(balls):
    count = 0
    global stopflag
    for i in range(len(balls)):
        if balls[i].player_color == red:
            count += 1
    if count >= len(balls)-1:
        stopflag = False
        label = my_font_GO.render("Game Over!", 0, white, (100, 100, 100))
        screen.blit(label, (550, 380))
        textReStart = my_font.render('New Game', True, black)
        screen.blit(textReStart, (600, 430))
        if 450 <= mouseClick_x <= 650 and 350 <= mouseClick_y <= 550:
            resetgame(balls)

def resetgame(balls):
    global points
    global stopflag
    for i in range(1, len(balls)):
        balls[i].player_color = blue
    stopflag = True
    points = 0


def game():
    balls.append(Circle(random.randint(100, 1100),random.randint(50, 650), 4, 4))
    balls[0].player_color = corona
    balls.append(Circle(random.randint(100, 1100), random.randint(50, 650), 4, 4))
    for i in range(25):
        balls.append(Circle(random.randint(150, 1100)-random.randint(10,20), random.randint(150, 600)+random.randint(10,20), random.randint(-4, 4)+1, random.randint(-4, 4)+1))

    textmoney = my_font.render('your money:', True, black)
    textCounterBlue = my_font.render('Blue counter:', True, black)
    textExplanation = my_font.render('To freeze the screen for 5 seconds, press S - Each use dropped 5 points', True, black)
    textAccurecy = my_font.render('Accurecy:', True, black)
    textBomb = my_font.render('Bomb - 10', True, red)
    Clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                mousecheck(balls)
                if 1200 <= mouseClick_x <= 1300 and 20 <= mouseClick_y <= 60:
                    bomb(balls)
            elif event.type == pygame.KEYDOWN:
                global points
                global stopflag
                if event.key == pygame.K_s:
                    if points >= 5:
                        stopflag = False
                        points -= 5

        screen.fill(white)

        screen.blit(textmoney, (10, 20))
        screen.blit(my_font.render(str(points), True, black), (130, 20))

        screen.blit(textCounterBlue, (10, 50))
        screen.blit(my_font.render(str(blueCount), True, black), (130, 50))

        screen.blit(textAccurecy, (10, 80))
        global temp
        screen.blit(my_font.render(str(temp), True, black), (100, 80))

        screen.blit(textExplanation, (10, 110))
        screen.blit(textBomb, (1200, 40))

        endgame(balls)

        colide(balls)
        [Circle.bouncing_rect() for Circle in balls]
        [Circle.update() for Circle in balls]
        [Circle.draw() for Circle in balls]
        pygame.display.update()
        clock.tick(60)
game()
pygame.quit()