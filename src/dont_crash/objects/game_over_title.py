import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT
        
class GameOverTitle:
    def __init__(self, time_alive):
        self.time_alive = time_alive
        self.text = f"Game Over! Time Alive: {self.time_alive:.2f}s"
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.x = WINDOW_WIDTH // 2 - 150
        self.y = WINDOW_HEIGHT // 2
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def draw(self, surface):
        surface.blit(self.rendered_text, (self.x, self.y))
