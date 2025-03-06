import pygame
from constants import *
from player import *

def main():
    pygame.init()

    # get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # add functionality to close button on game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # limit game to 60 fps and track delta time
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()