import pygame
import sys
from config import WIDTH, HEIGHT, FPS, screen
from pixel_structures import pixels_as_list
from algorithms import *


pygame.init()
pygame.display.set_caption("Game")



def main():

    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((0, 0, 0))

        explosion(speed=.7)

        for entity in pixels_as_list:
            screen.blit(entity.surf, entity.rect)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()