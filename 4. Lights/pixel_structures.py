from config import NUMBER_OF_PIXELS_X, NUMBER_OF_PIXELS_Y, PIXEL_LENGTH
from pixel import Pixel
from pygame.math import Vector2



pixels_as_list: list[Pixel] = [Pixel(Vector2(PIXEL_LENGTH * i + PIXEL_LENGTH / 2, 
                                             PIXEL_LENGTH * j + PIXEL_LENGTH / 2)) 
                                for i in range(NUMBER_OF_PIXELS_X)
                                for j in range(NUMBER_OF_PIXELS_Y)]


pixels_as_matrix: list[list[Pixel]] = [[pixels_as_list[j + i * NUMBER_OF_PIXELS_Y] 
                                        for i in range(NUMBER_OF_PIXELS_X)] 
                                        for j in range(NUMBER_OF_PIXELS_Y)]




        
