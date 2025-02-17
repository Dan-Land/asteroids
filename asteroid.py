import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), 12)
        pygame.draw.circle(screen, "black", (self.position.x, self.position.y), 10)
    
    def update(self, dt):
        use_bounce = False
        self.position += self.velocity * dt
        if use_bounce == True:
            if self.position.x >= 1285:
                self.velocity.x *= -1
                self.position.x = 1280
            elif self.position.x <= -5:
                self.velocity.x *= -1
                self.position.x = 0
            elif self.position.y <= -5:
                self.velocity.y *= -1
                self.position.y = 0
            elif self.position.y >= 725:
                self.velocity.y *= -1
                self.position.y = 720