try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from util import *
    from constants import *
    from tile import Tile
    from pygame.locals import *
    from pool import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)

class Grid():
    def __init__(self, screen, variation):
        self.screen = screen
        self.size = None
        self.ships = None
        self.cells = None
        self.variation = variation
        self.rect = None
        self.surf = None
        self.reinit()

    def reinit(self):
        if self.variation == HANGAR:
            self.size = HANGAR_SIZE
            self.ships = [None for _ in range(self.size[0] * self.size[1])]
            self.cells = [
                Tile(
                    self.variation,
                    i,
                    (
                        (i % self.size[0])*(HANGAR_BLOCK_SIZE[0] + HANGAR_BLOCK_PADDING) + HANGAR_RECT_OBJ_POS[0],
                        (i // self.size[0])*(HANGAR_BLOCK_SIZE[1] + HANGAR_BLOCK_PADDING) + HANGAR_RECT_OBJ_POS[1]
                    )
                )
                for i in range(self.size[0] * self.size[1])
            ]
            self.rect = pygame.Rect(HANGAR_RECT_POS, HANGAR_RECT_SIZE)
            self.surf = pygame.Surface(HANGAR_RECT_SIZE)
            self.surf.fill(COLOR_HANGAR)
            self.rect_outline = pygame.Rect(HANGAR_RECT_OUTLINE_POS, HANGAR_RECT_OUTLINE_SIZE)
            self.surf_outline = pygame.Surface(HANGAR_RECT_OUTLINE_SIZE)
            self.surf_outline.fill(COLOR_HANGAR_OUTLINE)
            self.surf.set_alpha(100)
            self.surf_outline.set_alpha(100)
        if self.variation == BATTLE:
            self.size = BATTLE_SIZE
            self.ships = [None for _ in range(self.size[0] * self.size[1])]
            self.cells = [
                Tile(
                    self.variation,
                    i,
                    (
                        (i % self.size[0])*(BATTLE_BLOCK_SIZE[0] + BATTLE_BLOCK_PADDING) + BATTLE_RECT_OBJ_POS[0],
                        (i // self.size[0])*(BATTLE_BLOCK_SIZE[1] + BATTLE_BLOCK_PADDING) + BATTLE_RECT_OBJ_POS[1]
                    )
                )
                for i in range(self.size[0] * self.size[1])
            ]
            self.rect = pygame.Rect(BATTLE_RECT_POS, BATTLE_RECT_SIZE)
            self.surf = pygame.Surface(BATTLE_RECT_SIZE)
            self.surf.fill(COLOR_BATTLE)
            self.rect_outline = pygame.Rect(BATTLE_RECT_OUTLINE_POS, BATTLE_RECT_OUTLINE_SIZE)
            self.surf_outline = pygame.Surface(BATTLE_RECT_OUTLINE_SIZE)
            self.surf_outline.fill(COLOR_BATTLE_OUTLINE)
            self.surf.set_alpha(100)
            self.surf_outline.set_alpha(100)
        if self.variation == MARKET:
            self.size = MARKET_SIZE
            self.ships = [None for _ in range(self.size[0] * self.size[1])]
            self.cells = [
                Tile(
                    self.variation,
                    i,
                    (
                        (i % self.size[0])*(MARKET_BLOCK_SIZE[0] + MARKET_BLOCK_PADDING) + MARKET_RECT_OBJ_POS[0],
                        (i // self.size[0])*(MARKET_BLOCK_SIZE[1] + MARKET_BLOCK_PADDING) + MARKET_RECT_OBJ_POS[1]
                    )
                )
                for i in range(self.size[0] * self.size[1])
            ]
            self.rect = pygame.Rect(MARKET_RECT_POS, MARKET_RECT_SIZE)
            self.surf = pygame.Surface(MARKET_RECT_SIZE)
            self.surf.fill(COLOR_MARKET)
            self.rect_outline = pygame.Rect(MARKET_RECT_OUTLINE_POS, MARKET_RECT_OUTLINE_SIZE)
            self.surf_outline = pygame.Surface(MARKET_RECT_OUTLINE_SIZE)
            self.surf_outline.fill(COLOR_MARKET_OUTLINE)
            self.surf.set_alpha(100)
            self.surf_outline.set_alpha(100)

    def fill_market(self, pool, tier):
        ships_to_add = pool.get_ships(tier)
        for i in range(len(self.ships)):
            self.ships[i] = pool.pool_dict[ships_to_add[i]]
            self.ships[i].rect.move_ip(
                self.cells[i].rect.x - MARKET_TILE_X_OFFSET,
                self.cells[i].rect.y - MARKET_TILE_Y_OFFSET
            )

    def render(self):
        self.screen.blit(self.surf_outline, self.rect_outline)
        self.screen.blit(self.surf, self.rect)
        for c in self.cells:
            self.screen.blit(c.surf, c.rect)
        for s in self.ships:
            if s:
                self.screen.blit(s.surf, s.rect)