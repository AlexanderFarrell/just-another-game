import pygame

sprites = []

class Sprite:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x
        self.y
        self.sprites(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def delete(self):
        sprites.remove(self)