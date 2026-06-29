import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((1000,800), pygame.RESIZABLE)
game_icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Car racing game")


car = pygame.image.load('car_3.png')
car = pygame.transform.scale(car, (80, 150))
clock = pygame.time.Clock()


green = (120, 180, 80)
grey = (128,128,128)
black = (0,0,0)
white = (255,255,255)

quit_game = False

car_x = 385
car_y = 580

car_x_change = 0
car_y_change = 0

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car_x_change = 2
                car_y_change = 0
            if event.key == pygame.K_LEFT:
                car_x_change = -2
                car_y_change = 0

    car_x += car_x_change
    car_y += car_y_change

    screen.fill(green)

    pygame.draw.rect(screen, (60, 60, 60), [200, 0, 600, 800])
    pygame.draw.rect(screen, white, [200, 0, 10, 800])
    pygame.draw.rect(screen, white, [800, 0, 10, 800])

    divider_x_positions = [350, 500, 650]
    for x in divider_x_positions:
        for y in range(0, 800, 60):
            pygame.draw.rect(screen, white, [x, y, 5, 40])

    for y in range(0, 80, 60):
        pygame.draw.rect(screen, white, [495, y, 0, 40])

    screen.blit(car, (car_x, car_y))
    pygame.display.update()

pygame.quit()
quit()