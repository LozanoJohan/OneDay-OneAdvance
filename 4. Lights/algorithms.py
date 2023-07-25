from pixel_structures import pixels_as_list, pixels_as_matrix
from config import PIXEL_LENGTH, NUMBER_OF_PIXELS_X

from pygame import Color
from lib import utils
import pygame
import math
import random



def rainbow(): 

    color = Color(255, 255, 255)
    time = pygame.time.get_ticks() / 1000

    for y_pixels in pixels_as_matrix:

        for i, x_pixel in enumerate(y_pixels):
            
            hue = math.sin(time + i / len(y_pixels)) * 299 / 2 + 150
            color.hsva = (hue, 100, 100, 100)

            x_pixel.set_color(color)
            x_pixel.draw()
    
    pygame.display.flip()



def explosion(wait_time: int = 25):

    '''Boom
    params:
    wait_time: int - Time in miliseconds to wait each layer to color.
    '''

    color: Color = utils.random_color_by_hue()
    radius = random.randint(1, PIXEL_LENGTH / 2)

    center_pixel = random.choice(pixels_as_list)
    center_pixel.set_color(color)

    pixels_already_colored = set()

    for layer in range(0, radius * int(PIXEL_LENGTH), int(PIXEL_LENGTH)):
        
        color.r -= color.r // radius
        color.g -= color.g // radius
        color.b -= color.b // radius

        for pixel in pixels_as_list:

            if (pixel.pos - center_pixel.pos).length() < layer and pixel not in pixels_already_colored:
                
                pixel.set_color(color)
                pixel.draw()

                pixels_already_colored.add(pixel)
        

        pygame.display.flip()
        pygame.time.delay(wait_time)



def wave(t: int, speed: int = 2):

    color = Color(255, 255, 255)
    t = t * speed

    for y, row in enumerate(pixels_as_matrix):

        for x, pixel in enumerate(row):

            hue = 180 * math.cos(t) * math.sin(x * math.pi/ NUMBER_OF_PIXELS_X) * math.sin(7 + (y * math.pi/ NUMBER_OF_PIXELS_X)) + 180
            color.hsva = (hue, 100, 100, 100)

            pixel.set_color(color)
            pixel.draw()
        
    pygame.display.flip()


