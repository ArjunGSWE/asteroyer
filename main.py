import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
import sys


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    field = AsteroidField()

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    dt = 0

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("GAME OVER")
                sys.exit()

        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)

        dt = clock.tick(60) / 1000

        pygame.display.flip()


if __name__ == "__main__":
    main()
