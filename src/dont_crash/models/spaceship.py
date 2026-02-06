import pygame
import numpy as np

from config import GRAVITY_STRENGTH, SPACESHIP_TURN_SPEED, WINDOW_WIDTH, WINDOW_HEIGHT
from utils import smootherstep

class SpaceShip:
    def __init__(self, x, y):
        
        self.mass = 2000.0  # kg
        
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.vel_x = 0.0
        self.vel_y = 0.0
        
        self.gravity = GRAVITY_STRENGTH
        self.thrust_force = 800000.0 # N
        
        self.drag_coef = 0.6
        self.turn_speed = SPACESHIP_TURN_SPEED
        
        self.angle = 90.0
        self.angle_vel = 0.0
        
        # Input Flags
        self.thrusting = False
        self.turning_left = False
        self.turning_right = False
        
        self.smootherstep_thust = 0.0
        self.smootherstep_turn = 0.0
        
        # Graphics
        self.width = 30
        self.height = 40
        self.original_image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.polygon(self.original_image, (255, 255, 255), 
                            [(self.width//2, 0), (0, self.height), (self.width//2, self.height * 4/5), (self.width, self.height)])
        
        self.time_since_thrust_start = 0.0
        self.time_since_turn_start = 0.0
        

    def update(self, delta_time):
        
        if self.thrusting:
            self.time_since_thrust_start += delta_time
        else:
            self.time_since_thrust_start = 0.0
        
        if self.turning_left or self.turning_right:
            self.time_since_turn_start += delta_time
        else:
            self.time_since_turn_start = 0.0
        
        F_thr_x = 0.0
        F_thr_y = 0.0
        
        G = self.gravity * self.mass
        
        if self.thrusting:
            self.smootherstep_thust = smootherstep(self.time_since_thrust_start, duration=0.5)
            rad = np.deg2rad(self.angle)
            F_thr_x = self.thrust_force * np.cos(rad)
            F_thr_y = self.thrust_force * np.sin(rad) * self.smootherstep_thust
            
            
        # Wrap X boundaries
        self.pos_x = self.pos_x % WINDOW_WIDTH
        
        # Floor and Ceiling for Y boundaries
        acc_y = 0.0
        
        
        # Update angle
        self.smootherstep_turn = smootherstep(self.time_since_turn_start, duration=0.3)
        
        if self.turning_left:
            self.angle_vel = self.turn_speed
        elif self.turning_right:
            self.angle_vel = -self.turn_speed
        else:
            self.angle_vel = 0.0
        
        self.angle += self.angle_vel * delta_time  * self.smootherstep_turn
        self.angle = self.angle % 360.0
            
        
        G = self.gravity * self.mass

        F_air_x = self.drag_coef * self.vel_x * abs(self.vel_x)
        F_air_y = self.drag_coef * self.vel_y * abs(self.vel_y)
        
        
        acc_x = (F_thr_x - F_air_x ) / self.mass
        acc_y = (-F_thr_y - F_air_y + G) / self.mass         
        
        # Update velocity with acceleration
        self.vel_y += acc_y * delta_time
        self.vel_x += acc_x * delta_time
        
        # Update position with velocity
        self.pos_y += self.vel_y * delta_time
        self.pos_x += self.vel_x * delta_time
        
        if self.pos_y >= WINDOW_HEIGHT:
            self.pos_y = WINDOW_HEIGHT
            self.vel_y = 0.0
        elif self.pos_y <= 0:
            self.pos_y = 0.0
            self.vel_y = 0.0
        

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.original_image, self.angle - 90)
        new_rect = rotated_image.get_rect(center=(self.pos_x, (self.pos_y)))
        
        if self.thrusting:
            rad = np.deg2rad(self.angle)
            flame_x = self.pos_x - (20 * np.cos(rad))
            flame_y = self.pos_y + (20 * np.sin(rad))
            pygame.draw.circle(surface, (255, 100, 0), (int(flame_x), int(flame_y)), 8*self.smootherstep_thust)
    
        surface.blit(rotated_image, new_rect)
        
