import pygame
import os

from config import FPS, WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from states import StartState, GameState, GameOverState


def main():
    pygame.init()
        
    os.environ['SDL_VIDEO_WINDOW_POS'] = '1' # Center the window on the screen

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    current_state = StartState(window, clock)

    _running = True
    
    time_step = 1000 / FPS
    last_update_time = pygame.time.get_ticks()
    delta_time_ms = time_step

    while _running:
        current_time = pygame.time.get_ticks()
        delta_time_ms = current_time - last_update_time
        last_update_time = current_time
        
        time_alive = 0.0
        
        # Handle events
        events = pygame.event.get()
        navigation, info = current_state.handle_events(events)
        
        
        match navigation:
            case "start_game":
                # Start a new game by switching to the GameState
                current_state = GameState(window, clock)
                
            case "game_over":
                # Switch to the GameOverState, passing the time alive information
                time_alive = info.get("time_alive", 0.0)
                current_state = GameOverState(window, clock, time_alive=time_alive)
            
            case "exit":
                # Exit the game loop and quit the game
                _running = False
                break
            
            case _:
                # No navigation change, continue with the current state
                pass
            
                
        current_state.update(delta_time_ms/1000)
        current_state.render()
        pygame.display.flip()
        clock.tick(FPS)
        

    # Quit game when loop ends
    pygame.quit()


if __name__ == "__main__":
    main()

