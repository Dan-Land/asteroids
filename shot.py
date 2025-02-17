import pygame
import constants
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        
        # Create the bullet's appearance
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        use_bounce = False
        self.position += self.velocity * dt
        # Keep the rect in sync with the position
        self.rect.center = self.position
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