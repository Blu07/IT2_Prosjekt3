
import pygame

class TimeAliveText:
    def __init__(self):
        self.time_alive = 0.0
        self.text = f"Time Alive: {self.time_alive:.2f}s"
        self.font = pygame.font.Font(None, 36)
        self.color = (255, 255, 255)
        self.x = 10
        self.y = 50
        
        self.rendered_text = self.font.render(self.text, True, self.color)
    
    def set_time_alive(self, time_alive: float | None = None):
        if time_alive is None:
            time_alive = self.time_alive
        self.rendered_text = self.font.render(f"Time Alive: {time_alive:.2f}s", True, self.color)
    
    def update(self, delta_time):
        self.time_alive += delta_time
        self.set_time_alive(self.time_alive)
    
    def draw(self, surface):
        surface.blit(self.rendered_text, (self.x, self.y))
