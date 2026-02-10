import pygame

from config import WINDOW_WIDTH, WINDOW_HEIGHT

class RestartButton:
    """ A button object that displays "Restart Game" and can detect clicks to restart the game.
    """
    
    def __init__(self):
        """ Initialize the restart button positioned at the center-bottom of the screen.
        """
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

    def draw(self, surface: pygame.Surface) -> None:
        """ Draw the button on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the button on.
        """
        pygame.draw.rect(surface, self.background_color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_pressed(self, mouse_pos: tuple[int, int]) -> bool:
        """ Check if the button is pressed based on the mouse position.

        Args:
            mouse_pos (tuple[int, int]): The current position of the mouse cursor.
        
        Returns:
            bool: True if the mouse position is within the button's rectangle, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)