import pygame

from config import WINDOW_WIDTH

class StartButton:
    """ A button object that displays "Start Game" and can detect clicks to start the game.
    """
    
    def __init__(self):
        """ Initialize the start button.
        """
        
        self.x = WINDOW_WIDTH // 2 - 100
        self.y = 300
        self.width = 200
        self.height = 50
        self.text = "Start Game"
        self.font = pygame.font.Font(None, 36)
        self.background_color = (100, 200, 100)
        self.text_color = (0, 0, 0)
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

    def draw(self, surface) -> None:
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
        """
        
        return self.rect.collidepoint(mouse_pos)