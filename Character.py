import pygame
class Aidn5(pygame.sprite.Sprite):

    def __init__(self, x):
        self.pressed_a = False
        self.pressed_d = False
        self.x1 = x
        self.player_pos = (self.x1, 780)
        self.speed = 10
        super().__init__()

    def start(self, screen):
        pygame.draw.circle(screen, "red", self.player_pos, 40)


    def move_left(self):
        self.x1 -= self.speed


    def move_right(self):
        self.x1 += self.speed

    def character_update(self, screen):
        self.player_pos = (self.x1, 780)
        pygame.draw.circle(screen, "red", self.player_pos, 40)



