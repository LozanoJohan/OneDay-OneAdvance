from pixel_structures import pixels_as_list, pixels_as_matrix
from config import PIXEL_LENGTH, screen

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
            

def explosion(speed, radius: int = None, center: tuple = None, color: Color = None):

    def random_color():

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        return Color(r, g, b)
    

    def fade_out(color: Color):

        _color: Color = color or random_color()
    radius = radius or random.randint(1, PIXEL_LENGTH / 2)

    center_pixel = random.choice(pixels_as_list)
    center_pixel.set_color(_color)

    pixels_already_colored = set()

    for layer in range(0, radius * int(PIXEL_LENGTH), int(PIXEL_LENGTH)):
        
        _color.r -= _color.r // radius
        _color.g -= _color.g // radius
        _color.b -= _color.b // radius

        for pixel in pixels_as_list:

            if (pixel.pos - center_pixel.pos).length() < layer and pixel not in pixels_already_colored:
                
                pixel.set_color(_color)
                pixels_already_colored.add(pixel)

    
    _color: Color = color or random_color()
    radius = radius or random.randint(1, PIXEL_LENGTH / 2)

    center_pixel = random.choice(pixels_as_list)
    center_pixel.set_color(_color)

    pixels_already_colored = set()

    for layer in range(0, radius * int(PIXEL_LENGTH), int(PIXEL_LENGTH)):
        
        _color.r -= _color.r // radius
        _color.g -= _color.g // radius
        _color.b -= _color.b // radius

        for pixel in pixels_as_list:

            if (pixel.pos - center_pixel.pos).length() < layer and pixel not in pixels_already_colored:
                
                pixel.set_color(_color)
                pixels_already_colored.add(pixel)


    fade_out(_color)
            
            


            


    




    