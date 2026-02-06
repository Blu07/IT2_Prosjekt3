import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT

class RestartButton:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2 - 100
        self.y = WINDOW_HEIGHT // 2 + 50
        self.width = 200
        self.height = 40
        self.text = "Restart Game"
        self.font = pygame.font.Font(None, 36)
        self.background_color = (255, 0, 255)
        self.text_color = (255, 255, 255)
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.background_color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_pressed(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)