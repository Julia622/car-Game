import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((1000,800), pygame.RESIZABLE)
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car racing game")

green = (120, 180, 80)
grey = (128,128,128)
black = (0,0,0)
white = (255,255,255)

quit_game = False

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    screen.fill(green)

    pygame.draw.rect(screen, (60, 60, 60), [300, 0, 400, 800])
    pygame.draw.rect(screen, white, [300, 0, 10, 800])
    pygame.draw.rect(screen, white, [690, 0, 10, 800])

    divider_x_positions = [400, 500, 600]
    for x in divider_x_positions:
        for y in range(0, 800, 60):
            pygame.draw.rect(screen, white, [x, y, 5, 40])

    for y in range(0, 800, 60):
        pygame.draw.rect(screen, white, [495, y, 0, 40])

    pygame.display.update()

pygame.quit()
quit()
