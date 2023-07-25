import pygame
import sys
from config import FPS, screen
import algorithms


TIME_BETWEEN_ANIMATIONS = 3
ANIMATIONS = [algorithms.rainbow, algorithms.explosion, algorithms.wave]


pygame.init()
pygame.display.set_caption("Game")


def main():

    clock = pygame.time.Clock()

    while True:

        t = (pygame.time.get_ticks() / 1000) % (len(ANIMATIONS) * TIME_BETWEEN_ANIMATIONS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(FPS)
        

        if t < TIME_BETWEEN_ANIMATIONS:
            ANIMATIONS[0]()

        elif t < 2 * TIME_BETWEEN_ANIMATIONS:
            ANIMATIONS[1]()

        elif t < 3 * TIME_BETWEEN_ANIMATIONS:
            ANIMATIONS[2](t)




if __name__ == '__main__':

    main()
    
    
