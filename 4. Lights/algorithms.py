import config
from pixel_structures import pixels_as_list, pixels_as_matrix
from config import PIXEL_LENGTH

from pygame import Color
import pygame
import math
import random
import time


def sin(): 

    color = Color(255, 255, 255)
    time = pygame.time.get_ticks() / 1000

    for y_pixels in pixels_as_matrix:

        for i, x_pixel in enumerate(y_pixels):
            
            hue = math.sin(time + i / len(y_pixels)) * 299 / 2 + 150
            color.hsva = (hue, 100, 100, 100)

            x_pixel.set_color(color)
            

def explosion(radius: int, speed, center: tuple = None, color: Color = None):

    _color: Color = color or random_color()

    center_pixel = random.choice(pixels_as_list)
    center_pixel.set_color(_color)

    pixels_already_colored = set()

    for layer in range(0, radius * int(PIXEL_LENGTH), int(PIXEL_LENGTH)):
        
        _color.r -= _color.r // radius
        print(_color.r)

        for pixel in pixels_as_list:

            if (pixel.pos - center_pixel.pos).length() < layer and pixel not in pixels_already_colored:
                
                pixel.set_color(_color)
                pixels_already_colored.add(pixel)

                print(pixel.color)
        
        for entity in pixels_as_list:
            config.display_surface.blit(entity.surf, entity.rect)
        time.sleep(speed)

        print("--------------------")
            
            


            


    




def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return Color(r, g, b)