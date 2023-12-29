
# Import sys and time for some standard functions
import sys, time

# Import the pygame library for graphics functions
import pygame

# Initialize the pygame library
pygame.init()

# Create a window of a specified size
screen = pygame.display.set_mode( (1920,1080) )

# Load the ball.gif image and save it's size (bounding box)
ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# Draw a black background (RGB is 0,0,0)
screen.fill( (0,0,0) )

# Draw the ball image to the screen 
screen.blit(ball, ballrect)

# Display the screen to the window
pygame.display.flip()

# Sleep for a 5 seconds before we exit
time.sleep(5)

