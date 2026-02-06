import pygame

from states import State

from objects import StartTitle
from objects import StartButton

class StartState(State):
    """ State for the initial screen shown at game launch.
    """
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock):
        """ Initialize the StartState with a heading text and a start button.
        """
        super().__init__(window, clock)
                
        self.title = StartTitle()
        self.start_button = StartButton()
    
    
    def handle_events(self, events: list[pygame.event.Event]) -> tuple[str | None, dict]:
        """ Handle standard events and start button presses.

        Args:
            events (list[pygame.event.Event]): List of pygame events to handle.

        Returns:
            tuple[str | None, dict]: A tuple where the first element is a string indicating the next state to navigate to (e.g. "start_game", "exit"), and the second element is a dictionary containing any relevant information to pass to the next state.
        """
              
        navigation, info = super().handle_events(events) # Handle quit and escape events
        
        # Handle start button click
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.start_button.is_pressed(pygame.mouse.get_pos()):
                    navigation = "start_game"
            
                
        return navigation, info
    
    def render(self) -> None:
        """ Draw background, title text and start button.
        """
        self.window.fill((0, 0, 0))
        
        self.title.draw(self.window)
        self.start_button.draw(self.window)

