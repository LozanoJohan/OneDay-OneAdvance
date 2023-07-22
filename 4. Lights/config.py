import pygame


HEIGHT = 640
WIDTH = 1280

HEIGHT_WIDTH_RATIO = HEIGHT / WIDTH

FPS = 60

NUMBER_OF_PIXELS_X = 40
NUMBER_OF_PIXELS_Y = int(NUMBER_OF_PIXELS_X * HEIGHT_WIDTH_RATIO)

PIXEL_LENGTH = WIDTH / NUMBER_OF_PIXELS_X

FramePerSec = pygame.time.Clock()
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")