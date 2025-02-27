import pygame
character_image = "./images/character.png"
class Aidn5(pygame.sprite.Sprite):

    def __init__(self, x):
        self.image = pygame.transform.scale2x(pygame.image.load(character_image)).convert_alpha()
        self.x = 512
        self.player_pos = (self.x, 780)
        self.character = pygame.image.load(character_image)
        self.speed = 5
        super().__init__()

    def start(self, screen):
        pygame.draw.circle(screen, "red", self.player_pos, 40)


    def move_left(self):
        self.x += self.speed
        pygame.display.update()


    def move_right(self):
        self.x -= self.speed
        pygame.display.update()