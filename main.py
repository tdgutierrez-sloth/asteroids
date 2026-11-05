import pygame
import sys

# don't use <name>.py for the import use just <name>
from constants import *
from logger import log_state
from logger import log_event

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
#    print("Hello from asteroids!")
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0.0

	#x = SCREEN_WIDTH/2
	#y = SCREEN_HEIGHT/2
	#

	# set up groups and containers
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# allocate classes to groups
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	Shot.containers = (shots, drawable, updatable)

	# create instances
	my_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	my_asteroidfield = AsteroidField()

	# game loop
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		updatable.update(dt)
		#print("drawable count:", len(drawable), "asteroids count:", len(asteroids))

		# check player collision with asteroid
		for roid in asteroids:
			if roid.collides_with(my_player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		# check shot collision with asteroid
		for roid in asteroids:
			for a_shot in shots:
				if a_shot.collides_with(roid):
					log_event("asteroid_shot")
					a_shot.kill()
					roid.split()



		for thing in drawable:
			#print(type(thing))
			thing.draw(screen)

		# rendering
		pygame.display.flip()

		dt = clock.tick(60) / 1000


if __name__ == "__main__":
	main()
