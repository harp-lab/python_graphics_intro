import sys, time
import pygame

pygame.init()
screensize = width, height = 1920, 1080
screen = pygame.display.set_mode(screensize)

# Load the ball.gif image and save an initial bounding box
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# Move the ball to 100, 100
ballrect = ballrect.move([100, 100])

# Draw a black background (RGB is 0,0,0)
screen.fill( (0,0,0) )

# Draw the ball image to the screen 
screen.blit(ball, ballrect)

# Display the screen to the window
pygame.display.flip()

# Wait until the user tells us to exit, then call sys.exit
while True:
    # Loop through all game events, forever
    for event in pygame.event.get():
        # Ignore all pygame events except the QUIT event
        if event.type == pygame.QUIT: sys.exit()


