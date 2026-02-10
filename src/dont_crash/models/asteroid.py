import pygame
import numpy as np

from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Asteroid:
    """ Represents an asteroid object in the game that moves in a random direction and wraps around screen edges.
    """
    
    def __init__(self, x, y, size, vel):
        """ Initialize an Asteroid with position, size, and velocity.

        Args:
            x (float): The initial x-coordinate of the asteroid.
            y (float): The initial y-coordinate of the asteroid.
            size (float): The radius of the asteroid in pixels.
            vel (float): The velocity of the asteroid in pixels per second.
        """
        self.pos_x = x
        self.pos_y = y
        self.size = size  # radius in pixels
        self.direction = np.random.rand() * 2 * np.pi
        self.vel = vel  # pixels per second
    
    def update(self, delta_time):
        """ Update the asteroid's position based on its velocity and direction.

        Args:
            delta_time (float): The time elapsed since the last frame in seconds.
        """
        self.pos_x += self.vel * np.cos(self.direction) * delta_time
        self.pos_y += self.vel * np.sin(self.direction) * delta_time
        
        self.pos_x = self.pos_x % WINDOW_WIDTH
        self.pos_y = self.pos_y % WINDOW_HEIGHT
        
    def draw(self, surface):
        """ Draw the asteroid as a circle on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the asteroid on.
        """
        pygame.draw.circle(surface, (150, 150, 150), (int(self.pos_x), int(self.pos_y)), self.size)
        

