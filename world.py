class Tile:
    def __init__(self, image, is_solid):
        self.image = image
        self.is_solid = is_solid

class World:
    def __init__(self, tiles, map):
        self.map = map
        self.tiles = tiles

    def draw(self, screen):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                tile = int(cell)
                screen.blit(self.tiles[tile].image, (x, y))

        