from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.x, self.y = self.position.x, self.position.y


    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.x, self.y, new_radius)
        ast2 = Asteroid(self.x, self.y, new_radius)
        ast1.velocity = v1 * 1.2
        ast2.velocity = v2 * 1.2
        # Optionally, you may want to return the new asteroids
        return ast1, ast2
