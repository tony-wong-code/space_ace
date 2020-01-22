try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from util import *
    from constants import *
    from pygame.locals import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)

class Tile():
    def __init__(self, variation, id, pos):
        self.id = id
        self.variation = variation
        self.surf = None
        self.rect = None
        self.x = pos[0]
        self.y = pos[1]
        self.reinit()

    def reinit(self):
        if self.variation == HANGAR:
            self.surf, self.rect = load_png('hangar_tile.png')
            self.surf = pygame.transform.scale(self.surf, HANGAR_BLOCK_SIZE)
            self.rect.w = HANGAR_BLOCK_SIZE[0]
            self.rect.h = HANGAR_BLOCK_SIZE[1]
            self.rect.move_ip(self.x, self.y)
        if self.variation == BATTLE:
            self.surf, self.rect = load_png('battle_tile.png')
            self.surf = pygame.transform.scale(self.surf, BATTLE_BLOCK_SIZE)
            self.rect.w = BATTLE_BLOCK_SIZE[0]
            self.rect.h = BATTLE_BLOCK_SIZE[1]
            self.rect.move_ip(self.x, self.y)
        if self.variation == MARKET:
            self.rect = pygame.Rect((self.x, self.y), MARKET_BLOCK_SIZE)
            self.surf = pygame.Surface(MARKET_BLOCK_SIZE)
            self.surf.fill(COLOR_MARKET_TILE)
            self.surf.set_alpha(50)