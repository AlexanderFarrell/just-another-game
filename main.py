import pygame
from sprite import Sprite, sprites

clear_color =(0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))

def update_stuff():
    pass

def draw_stuff():
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break;
    for s in sprites:
        s.draw()
    screen.fill(clear_color)

    pygame.display.flip()

pygame.quit()