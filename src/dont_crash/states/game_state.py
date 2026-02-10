import pygame
import numpy as np

from config import WINDOW_WIDTH, WINDOW_HEIGHT, START_LIVES, MAX_ASTEROIDS, ASTEROID_SPAWN_INTERVAL, SPACESHIP_TURN_SPEED, GRAVITY_STRENGTH
from models import SpaceShip, Asteroid
from objects import TimeAliveText, LivesText
from utils import balls_collide
from .state import State
    
class GameState(State):
    """ State representing the active gameplay, managing spaceship, asteroids, and collision detection.
    """
    
    UP_KEYS = [pygame.K_w, pygame.K_UP]
    LEFT_KEYS = [pygame.K_a, pygame.K_LEFT]
    RIGHT_KEYS = [pygame.K_d, pygame.K_RIGHT]
    
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock):
        """ Initialize the GameState with a spaceship, asteroids, and UI elements.

        Args:
            window (pygame.Surface): The Pygame window surface where the game will render.
            clock (pygame.time.Clock): The Pygame clock object used for managing the frame rate.
        """
        super().__init__(window, clock)
        
        self.asteroids = []
        self.spaceship = SpaceShip(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        
        self.lives = START_LIVES
        self.time_alive = 0.0
        self.lives_text = LivesText()
        self.time_alive_text = TimeAliveText()
        
        self.time_since_thrust_start = 0.0
        self.time_since_turn_start = 0.0
        
        self.max_asteroids = MAX_ASTEROIDS
        self.asteroid_spawn_interval = ASTEROID_SPAWN_INTERVAL
        self.time_since_last_asteroid_spawn = 0.0
        
    def create_asteroid(self):
        """ Create and add a new asteroid to the game if the maximum has not been reached.
        """
        if len(self.asteroids) >= self.max_asteroids:
            return
        
        asteroid = Asteroid(
            x=np.random.randint(0, WINDOW_WIDTH),
            y=np.random.randint(0, WINDOW_HEIGHT),
            size=np.random.randint(10, 50),
            vel=np.random.randint(30, 100)
        )
        
        self.asteroids.append(asteroid)
        
    def remove_asteroid(self, asteroid):
        """ Remove an asteroid from the game.

        Args:
            asteroid (Asteroid): The asteroid object to remove from the game.
        """
        if asteroid in self.asteroids:
            self.asteroids.remove(asteroid)
    
    def handle_events(self, events: list[pygame.event.Event]) -> tuple[str | None, dict]:
        """ Handle keyboard controls, collision detection, and game-over conditions.

        Args:
            events (list[pygame.event.Event]): A list of Pygame events to process.
        
        Returns:
            tuple[str | None, dict]: A tuple where the first element indicates the next state (e.g. "game_over", "exit"),
                                and the second element is a dictionary containing game information to pass to the next state.
        """
        navigation, info = super().handle_events(events) # Handle quit and escape events
        
        # Set flags for spaceship controls
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.LEFT_KEYS: 
                    self.spaceship.turning_left = True
                if event.key in self.RIGHT_KEYS:
                    self.spaceship.turning_right = True
                if event.key in self.UP_KEYS:
                    self.spaceship.thrusting = True

            if event.type == pygame.KEYUP:
                if event.key in self.UP_KEYS:
                    self.spaceship.thrusting = False
                if event.key in self.LEFT_KEYS:
                    self.spaceship.turning_left = False
                if event.key in self.RIGHT_KEYS:
                    self.spaceship.turning_right = False
            
        
        # Check collision with asteroids
        for asteroid in self.asteroids:
            if balls_collide(asteroid.pos_x, asteroid.pos_y, asteroid.size,
                             self.spaceship.pos_x, self.spaceship.pos_y, 10):

                self.remove_asteroid(asteroid)
                self.lives -= 1
                self.lives_text.set_lives(self.lives)
                if self.lives <= 0:
                    # Game Over
                    navigation = "game_over"
                    info = {"time_alive": self.time_alive}
        
        return navigation, info
    
    def update(self, delta_time: float):
        """ Update game entities, spawn asteroids, and track time alive.

        Args:
            delta_time (float): The time elapsed since the last frame in seconds.
        """
        for asteroid in self.asteroids:
            asteroid.update(delta_time)
                
        self.spaceship.update(delta_time)
        
        self.time_alive_text.update(delta_time)
        self.time_alive += delta_time
        
        self.time_since_last_asteroid_spawn += delta_time
        if self.time_since_last_asteroid_spawn >= self.asteroid_spawn_interval:
            self.create_asteroid()
            self.time_since_last_asteroid_spawn = 0.0
                    
    
    def render(self) -> None:
        """ Draw all game entities including asteroids, spaceship, and UI elements on the screen.
        """
        self.window.fill((0, 0, 0))
        
        for asteroid in self.asteroids:
            asteroid.draw(self.window)
            
        self.spaceship.draw(self.window)
        self.lives_text.draw(self.window)
        self.time_alive_text.draw(self.window)
