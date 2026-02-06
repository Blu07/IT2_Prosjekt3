
import pygame

from config import WINDOW_WIDTH

class StartTitle:
    """ A Text object that displays the text "Don't Crash" as the heading on the start screen.
    """
    
    def __init__(self):
        """ Initialize the text object.
        """
        self.text = "Don't Crash"
        self.font = pygame.font.Font(None, 74)
        self.color = (255, 255, 255)
        self.x = WINDOW_WIDTH // 2 - 150
        self.y = 100
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def draw(self, surface) -> None:
        """ Draw the rendered text on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the text on.
        """
        
        surface.blit(self.rendered_text, (self.x, self.y))
