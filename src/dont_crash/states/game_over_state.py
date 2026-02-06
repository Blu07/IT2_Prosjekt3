import pygame

from states import State

from objects import GameOverTitle
from objects import RestartButton

class GameOverState(State):
    def __init__(self, window, clock, time_alive=0.0):
        super().__init__(window, clock)

        self.game_over_text = GameOverTitle(time_alive)
        self.restart_button = RestartButton()
        

    def handle_events(self, events) -> tuple[str | None, dict]:
        navigation, info = super().handle_events(events) # Handle quit and escape events
        
        # Handle restart button click
        for event in events:            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.restart_button.is_pressed(pygame.mouse.get_pos()):
                    navigation = "start_game"
                
            
        return navigation, info
    
    def render(self):
        self.window.fill((0, 0, 0))
        
        self.game_over_text.draw(self.window)
        self.restart_button.draw(self.window)
        