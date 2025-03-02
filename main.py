import pygame
from Character import Aidn5
from Difficulty import Difficulty
from Buttons import Buttons
pygame.init()
clock = pygame.time.Clock()
"""
           buttons = Buttons(text=start_button["text"], x_pos=200, y_pos=200, enabled=True,
                             screen=screen, size_x=start_button["width"], size_y=start_button["height"])
           buttons.draw()
           if buttons.check_click():
               diff.start()
               running = False """

screen = pygame.display.set_mode((1024, 800))
diff = Difficulty()
running = True
background_list = ["./images/background_images/LEVEL0.jpg",]
level = 0
x = 512
aidn5 = Aidn5(x=x)
pressed_a = aidn5.pressed_a
pressed_d = aidn5.pressed_d
starting_menu = True
while running:
    background = pygame.image.load(background_list[level])
    aidn5.start(screen=screen)
    start_button = Buttons(text="Start", screen=screen, x_pos=800, y_pos=700, aliases=False, text_shadow=True, borders=True, line_thickness=5, border_color="red")
    while  starting_menu:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        diff.difficulti(screen=screen)

        start_button.draw()
        if start_button.check_click():
            starting_menu = False






        pygame.display.update()
        clock.tick(60)




    keys = pygame.key.get_pressed()
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    aidn5.start(screen=screen)

    if not keys[pygame.K_a]:
        pressed_a = False
    if not keys[pygame.K_d]:
        pressed_d = False
    if keys[pygame.K_a] and pressed_a == False and aidn5.x1 > 40:
        aidn5.move_left()
        pressed_a = True
        aidn5.character_update(screen=screen)

    if keys[pygame.K_d] and pressed_d == False and aidn5.x1 < 985:
        aidn5.move_right()
        pressed_d = True
        aidn5.character_update(screen=screen)

    pygame.display.update()
    clock.tick(60)
