import pygame
import sys
import config
from pixel_structures import pixels_as_list
from algorithms import *


def init_game():

    pygame.init()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        explosion(8, 1)

        config.display_surface.fill((0, 0, 0))

        

        pygame.display.update()
        config.FramePerSec.tick(config.FPS)

        #for pixel in pixels_as_list: pixel.set_color((0,0,0,0))

if __name__ == '__main__':
    init_game()