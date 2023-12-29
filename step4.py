import sys, time, random
import pygame

pygame.init()
screensize = width, height = 1920, 1080
screen = pygame.display.set_mode(screensize)

# Load the ball.gif image and save an initial bounding box
ball = pygame.image.load("ball.gif")

# Initialize N balls in a loop
N = 5
ballrect = ball.get_rect()
rects = []
xvs = []
yvs = []
for i in range(N):
    # Selects a random x and y velocity as either -1 or +1
    xvs.append(random.randrange(-1,2,2))
    yvs.append(random.randrange(-1,2,2))
    # Selects a random starting position
    rects.append(ballrect.move([random.randrange(100,1800),random.randrange(100,900)]))

# The "Game Loop" repeats forever until we exit:
while True:
    # Draw all N balls
    screen.fill( (0,0,0) )
    for i in range(N):
        screen.blit(ball, rects[i])
    pygame.display.flip()

    # Simulate ball movement for each ball
    for i in range(N):
        rects[i] = rects[i].move([xvs[i], yvs[i]])
        # If ball goes off the right side or left side, reverse the x velocity to "bounce"
        if rects[i].right > width or rects[i].left < 0: xvs[i] = -xvs[i]
        # If ball goes off the top side or bottom side, reverse the y velocity to "bounce"
        if rects[i].bottom > height or rects[i].top < 0: yvs[i] = -yvs[i]
    
    # Loop through all game events, forever
    for event in pygame.event.get():
        # Ignore all pygame events except the QUIT event
        if event.type == pygame.QUIT: sys.exit()

