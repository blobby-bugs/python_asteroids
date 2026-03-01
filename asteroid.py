import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)
        first_child_angle = self.velocity.rotate(split_angle)
        second_child_angle = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_child = Asteroid(self.position.x, self.position.y, new_radius)
        first_child.velocity = first_child_angle * 1.2
        
        second_child = Asteroid(self.position.x, self.position.y, new_radius)
        second_child.velocity = second_child_angle * 1.2