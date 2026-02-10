import pygame

from .state import State

from objects import GameOverTitle
from objects import RestartButton

class GameOverState(State):
    """ State displayed when the player loses all lives, showing final time alive and restart button.
    """
    
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock, time_alive: float = 0.0):
        """ Initialize the GameOverState with game over text and a restart button.

        Args:
            window (pygame.Surface): The Pygame window surface where the game over screen will render.
            clock (pygame.time.Clock): The Pygame clock object used for managing the frame rate.
            time_alive (float): The total time the player survived in the previous game, in seconds. Defaults to 0.0.
        """
        super().__init__(window, clock)

        self.game_over_text = GameOverTitle(time_alive)
        self.restart_button = RestartButton()
        
    def handle_events(self, events: list[pygame.event.Event]) -> tuple[str | None, dict]:
        """ Handle standard events and restart button presses.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        
        Returns:
            tuple[str | None, dict]: A tuple where the first element indicates the next state (e.g. "start_game", "exit"),
                                and the second element is an empty dictionary.
        """
        navigation, info = super().handle_events(events) # Handle quit and escape events
        
        # Handle restart button click
        for event in events:            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.restart_button.is_pressed(pygame.mouse.get_pos()):
                    navigation = "start_game"
                
            
        return navigation, info
    
    def render(self) -> None:
        """ Draw background, game over text, and restart button.
        """
        self.window.fill((0, 0, 0))
        
        self.game_over_text.draw(self.window)
        self.restart_button.draw(self.window)
        