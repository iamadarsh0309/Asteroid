import sys

import pygame
from asteroid import *
from constants import *
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = updatable, drawable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = shots, updatable, drawable

    asteroid_field = AsteroidField()

    clk = pygame.time.Clock()
    dt =  0 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

        for dr in drawable:
            dr.draw(screen)
        
        pygame.display.flip()
        delta_time = clk.tick(60)
        dt = delta_time / 1000.0
        # print(dt)

if __name__ == "__main__":
    main()
