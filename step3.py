import sys, time
import pygame

pygame.init()
screensize = width, height = 1920, 1080
screen = pygame.display.set_mode(screensize)

# Load the ball.gif image and save an initial bounding box
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# Initialize ball velocity
xv = 1
yv = 1

# The "Game Loop" repeats forever until we exit:
while True:
    # Draw repeatedly within the game loop so the ball can move
    screen.fill( (0,0,0) )
    screen.blit(ball, ballrect)
    pygame.display.flip()

    # Simulate ball movement
    ballrect = ballrect.move([xv, yv])
    # If ball goes off the right side or left side, reverse the x velocity to "bounce"
    if ballrect.right > width or ballrect.left < 0: xv = xv * -1
    # If ball goes off the top side or bottom side, reverse the y velocity to "bounce"
    if ballrect.bottom > height or ballrect.top < 0: yv = yv * -1
    
    # Loop through all game events, forever
    for event in pygame.event.get():
        # Ignore all pygame events except the QUIT event
        if event.type == pygame.QUIT: sys.exit()

