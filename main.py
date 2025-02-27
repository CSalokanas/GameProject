import pygame
import pynput.keyboard
from Character import Aidn5
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()
running = True
background_list = ["./images/background_images/LEVEL0.jpg",]
level = 0
x = 512
speed = 10
counter = 0
player_pos = (x, 780)
aidn5 = Aidn5(x=x)

while running:

    background = pygame.image.load(background_list[level])
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    counter = 0
    aidn5.start(screen=screen, player_pos=player_pos)
    if pynput.keyboard.Events.Press and counter == 0:
        print(x)
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
         x += speed

        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            x -= speed
    pygame.display.update()

    clock.tick(60)
pygame.quit()