import pygame

from config import START_LIVES

class LivesText:
    """ A text display showing the player's current number of lives.
    """
    
    def __init__(self):
        """ Initialize the lives text display with the starting number of lives.
        """
        self.num_lives = START_LIVES
        self.text = f"Lives: {self.num_lives}"
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.x = 10
        self.y = 10
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def set_lives(self, lives: int) -> None:
        """ Update the lives display to show the new number of lives.

        Args:
            lives (int): The current number of lives to display.
        """
        self.rendered_text = self.font.render(f"Lives: {lives}", True, self.color)
    
    def draw(self, surface: pygame.Surface) -> None:
        """ Draw the lives text on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the text on.
        """
        surface.blit(self.rendered_text, (self.x, self.y))