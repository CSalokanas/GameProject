import pygame
from Character import Aidn5

pygame.init()
screen = pygame.display.set_mode((1024, 800))
clock = pygame.time.Clock()
running = True
background_list = ["./images/background_images/LEVEL0.jpg",]
level = 0
x = 512
aidn5 = Aidn5(x=x)
pressed_a = aidn5.pressed_a
pressed_d = aidn5.pressed_d
while running:
    keys = pygame.key.get_pressed()
    background = pygame.image.load(background_list[level])
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    aidn5.start(screen=screen)

    if not keys[pygame.K_a]:
        pressed_a = False
    if not keys[pygame.K_d]:
        pressed_d = False
    if keys[pygame.K_a] and pressed_a == False:
        aidn5.move_left()
        pressed_a = True
        aidn5.update(screen=screen)

    if keys[pygame.K_d] and pressed_d == False:
        aidn5.move_right()
        pressed_d = True
        aidn5.update(screen=screen)

    pygame.display.update()
    clock.tick(60)
