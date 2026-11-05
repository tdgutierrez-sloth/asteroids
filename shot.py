import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
	def __init__(self, x: float, y: float):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
		#print("drawing asteroid at", self.position, "radius", self.radius)

	def update(self, dt: float) -> None:
		self.position += self.velocity * dt
