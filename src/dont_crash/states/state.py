import pygame

class State:
    """ Base class for game states. Each state should inherit from this class and implement the
        handle_events, update, and render methods.
    """
    
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock):
        """ Initialize a State with a window and clock objects.

        Args:
            window (pygame.Surface): The Pygame window surface where the state will render its content.
            clock (pygame.time.Clock): The Pygame clock object used for managing the frame rate and timing within the state.
        """
        
        self.window = window
        self.clock = clock
       
    
    def handle_events(self, events: list[pygame.event.Event]) -> tuple[str | None, dict]:
        """ Method to handle input events and other screen and game related events.
        
        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process for this state.
        
        Returns:
            tuple [str | None, dict]: The first element indicates the next state to navigate to (e.g. "start_game", "game_over", "exit"),
                                and the dictionary contains any relevant information to pass to the next state
        """
        
        navigation: str | None = None
        info: dict = {}
        
        for event in events:
            if event.type == pygame.QUIT:
                navigation = "exit"
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    navigation = "exit"
                
        return navigation, info


    def update(self, delta_time: float):
        """ Method to update screen elements, like speed and position, every frame.

        Args:
            delta_time (float): The time elapsed since the last frame, used for smooth and consistent updates.
        """
        
        pass # Specific functionality to be implemented by subclasses
    
    def render(self) -> None:
        """ Method to render the state on the screen every frame.
        This should include drawing all visual elements of the state.
        """
        self.window.fill((0, 0, 0))
        

