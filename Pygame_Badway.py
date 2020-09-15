import pygame
import sys

background_one = (0, 0, 0)
background_two = (255, 255, 255)

pygame.init()

window_width = 700
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Bad Example")

clock = pygame.time.Clock()

# BAD COUNTER >:(
frame_counter = 0

# Main loop of the program.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # DON'T DO THIS >:(
    frame_counter += 1

    if frame_counter > 20:
        screen.fill(background_two)
        frame_counter = 0
    elif frame_counter > 10:
        screen.fill(background_one)

    pygame.display.flip()

    clock.tick(20)