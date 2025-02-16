import pygame
from constants import *
from circleshape import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    asteroid_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    while True:
        dt = (asteroid_clock.tick(60) / 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("Black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()