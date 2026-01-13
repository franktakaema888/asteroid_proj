from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

from logger import log_event
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += (self.velocity * dt)

  def split(self):
    pygame.sprite.Sprite.kill(self)
    if self.radius < ASTEROID_MIN_RADIUS:
      return
    else:
      log_event("asteroid_split")
      r_angle = random.uniform(20, 50)
      v1 = self.velocity.rotate(r_angle)
      v2 = self.velocity.rotate(-r_angle)
      self.radius = self.radius - ASTEROID_MIN_RADIUS
      a1 = Asteroid(self.position.x, self.position.y, self.radius)
      a2 = Asteroid(self.position.x, self.position.y, self.radius)

      a1.velocity = v1 * 1.2
      a2.velocity = v2



    