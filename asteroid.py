import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y, radius,velocity = None):
        super().__init__(x,y,radius)
        self.radius = radius
        if velocity is None:
            angle = random.uniform(0,360)
            self.velocity = pygame.math.Vector2(1,0).rotate(angle)
        else:
            self.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20,50)

        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(random_angle * -1) *1.2

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2
        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)

        
        

    def draw(self,surface):
        pygame.draw.circle(surface, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        