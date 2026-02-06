import pygame
import numpy as np

from config import WINDOW_WIDTH, WINDOW_HEIGHT

class Asteroid:
    def __init__(self, x, y, size, vel):
        self.pos_x = x
        self.pos_y = y
        self.size = size  # radius in pixels
        self.direction = np.random.rand() * 2 * np.pi
        self.vel = vel  # pixels per second
    
    def update(self, delta_time):
        self.pos_x += self.vel * np.cos(self.direction) * delta_time
        self.pos_y += self.vel * np.sin(self.direction) * delta_time
        
        self.pos_x = self.pos_x % WINDOW_WIDTH
        self.pos_y = self.pos_y % WINDOW_HEIGHT
        
    def draw(self, surface):
        pygame.draw.circle(surface, (150, 150, 150), (int(self.pos_x), int(self.pos_y)), self.size)
        

