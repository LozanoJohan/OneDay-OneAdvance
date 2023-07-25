from pygame import Color
import random

def random_color_by_hue():

        h = random.randint(0, 360)

        color = Color('white')
        color.hsva = (h, 100, 100, 100)
        print(color)
        return color