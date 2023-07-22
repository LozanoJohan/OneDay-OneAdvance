from pygame.sprite import Sprite
from pygame import Color, Surface
from pygame.math import Vector2
from config import PIXEL_LENGTH


class Pixel(Sprite):
    def __init__(self, pos: Vector2):
        super().__init__()
        
        self.pos = pos
        self.surf = Surface((PIXEL_LENGTH, PIXEL_LENGTH))
        self.rect = self.surf.get_rect(center = pos)

        self.set_color(Color('black'))
    
    def set_color(self, color: Color):

        self.color = color
        self.surf.fill(self.color)
