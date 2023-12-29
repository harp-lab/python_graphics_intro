import sys, time, random
import pygame

pygame.init()
screensize = width, height = 1920, 1080
screen = pygame.display.set_mode(screensize)


# Load the ball.gif image and save an initial bounding box
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()


class Ball:
    def __init__(self):
        self.x = random.randrange(100, 1800)
        self.y = random.randrange(100, 900)
        # more granular random velocity
        self.xv = random.randrange(-10,11)/10.0
        self.yv = random.randrange(-10,11)/10.0
    def draw(self):
        # draw ball on the screen at this position, rounded to nearest integer (as now we have float precision)
        screen.blit(ball, ballrect.move([int(self.x)-ballrect.width/2, int(self.y)-ballrect.height/2]))
    def simulate(self):
        # simulate movement
        self.x += self.xv
        self.y += self.yv
        # simulate bouncing mechanic
        if self.x-ballrect.width/2 < 0 or self.x+ballrect.width/2 > width: self.xv = -self.xv
        if self.y-ballrect.height/2 < 0 or self.y+ballrect.height/2 > height: self.yv = -self.yv
        

# Initialize N balls in a loop
N = 15
balls = []
for i in range(N):
    balls.append(Ball())

# The "Game Loop" repeats forever until we exit:
while True:
    # Draw all N balls
    screen.fill( (0,0,0) )
    for i in range(N):
        balls[i].draw()
        balls[i].simulate()
    pygame.display.flip()
    
    # Loop through all game events, forever
    for event in pygame.event.get():
        # Ignore all pygame events except the QUIT event
        if event.type == pygame.QUIT: sys.exit()

