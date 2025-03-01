import pygame



class Buttons:
    def __init__(self, text,x_pos,y_pos,enabled, screen):
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.text = text
        self.text = self.font.render(text, True, (255, 255, 255))
        self.x = x_pos
        self.y = y_pos
        self.enabled = enabled
        self.screen = screen

    def draw(self,):
        button_rect = pygame.rect.Rect(self.x, self.y, 100, 50)
        pygame.draw.rect(surface=self.screen, color="gray", rect=button_rect)
        self.screen.blit(self.text, (self.x + 10, self.y + 10))