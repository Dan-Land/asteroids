import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)

        if velocity:
            self.velocity = velocity


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), (self.radius + 2))
        pygame.draw.circle(screen, "black", (self.position.x, self.position.y), self.radius)
        
    
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
        if self.position.x < -80 or self.position.x > 1360 or self.position.y < -80 or self.position.y > 800:
            self.kill()

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        ast_angle = random.uniform(20, 50)
        ast_velocity1 = self.velocity.rotate(ast_angle) * 1.2
        ast_velocity2 = self.velocity.rotate(-ast_angle) * 1.2
        ast_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, ast_radius, ast_velocity1)
        Asteroid(self.position.x, self.position.y, ast_radius, ast_velocity2)