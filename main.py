import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import *
from sys import exit

#source venv/bin/activate

def main():
    pygame.init()
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius = PLAYER_RADIUS)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for act in updatable:
            act.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print('Game Over!')
                exit()

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill(color=(0,0,0))

        for act in drawable:
            act.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
