import pygame

from config import START_LIVES

class LivesText:
    def __init__(self):
        self.num_lives = START_LIVES
        self.text = f"Lives: {self.num_lives}"
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.x = 10
        self.y = 10
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def set_lives(self, lives):
        self.rendered_text = self.font.render(f"Lives: {lives}", True, self.color)
    
    def draw(self, surface):
        surface.blit(self.rendered_text, (self.x, self.y))