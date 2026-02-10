
import pygame

class TimeAliveText:
    """ A text display showing how long the player has survived in the current game.
    """
    
    def __init__(self):
        """ Initialize the time alive text display with 0 seconds.
        """
        self.time_alive = 0.0
        self.text = f"Time Alive: {self.time_alive:.2f}s"
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.x = 10
        self.y = 50
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def set_time_alive(self, time_alive: float | None = None) -> None:
        """ Update the time alive display with the given time value.

        Args:
            time_alive (float | None): The time alive value to display in seconds. If None, uses the internal time_alive value.
        """
        if time_alive is None:
            time_alive = self.time_alive
        self.rendered_text = self.font.render(f"Time Alive: {time_alive:.2f}s", True, self.color)
    
    def update(self, delta_time: float) -> None:
        """ Update the internal time alive counter and refresh the display.

        Args:
            delta_time (float): The time elapsed since the last frame in seconds.
        """
        self.time_alive += delta_time
        self.set_time_alive(self.time_alive)
    
    def draw(self, surface: pygame.Surface) -> None:
        """ Draw the time alive text on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the text on.
        """
        surface.blit(self.rendered_text, (self.x, self.y))
