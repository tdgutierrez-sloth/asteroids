from ast import AST

import pygame
import random
from logger import log_event

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid (CircleShape):
	def __init__(self, x: float, y: float, radius: float):
		super().__init__(x, y, radius)
		#print("asteroid created", self.position, self.radius)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
		#print("drawing asteroid at", self.position, "radius", self.radius)

	def update(self, dt: float) -> None:
		self.position += self.velocity * dt

	def split(self) -> None:
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			new_angle = random.uniform(20,50)
			v1 = self.velocity.rotate(new_angle)
			v2 = self.velocity.rotate(-new_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid_1.velocity = v1
			asteroid_2.velocity = v2
