import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    # groups to categorize objects into
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2, shots)


    while True:
        dt = (asteroid_clock.tick(60) / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # screen fill
        screen.fill("Black")

        # draw sprites
        for drawing in drawable:
            drawing.draw(screen)
        shots.draw(screen)

        # update sprites
        updatable.update(dt)
        player.shot_timer -= dt
        shots.update(dt)

        # loop through asteroids to see if collision with player
        for ast in asteroid:
            if ast.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                # Draw circles around objects to visualize collision bounds
                pygame.draw.circle(screen, "red", (int(ast.position.x), int(ast.position.y)), ast.radius, 1)
                pygame.draw.circle(screen, "green", (int(shot.position.x), int(shot.position.y)), shot.radius, 1)
                if ast.check_collision(shot):
                    ast.kill()
                    shot.kill()
            
        pygame.display.flip()


if __name__ == "__main__":
    main()