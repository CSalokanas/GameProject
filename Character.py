import pygame
character_image = "./images/character.png"
class Aidn5(pygame.sprite.Sprite):

    def __init__(self, x):
        self.image = pygame.transform.scale2x(pygame.image.load(character_image)).convert_alpha()
        self.player_pos = (x, 780)
        super().__init__()

    def start(self, screen, player_pos):
        pygame.draw.circle(screen, "red", player_pos, 40)