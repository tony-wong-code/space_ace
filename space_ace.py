try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from util import *
    from constants import *
    from grid import Grid
    from pygame.locals import *
    from pool import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)


def main():
    pygame.init()
    tier = 5
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('S P A C E   A C E')
    clock = pygame.time.Clock()
    bg_surf, bg_rect = load_png('background.png')
    bg_surf = pygame.transform.scale(bg_surf, SCREEN_SIZE)
    bg_rect.w = SCREEN_WIDTH
    bg_rect.h = SCREEN_HEIGHT
    hangar = Grid(screen, HANGAR)
    player_side = Grid(screen, BATTLE)
    market = Grid(screen, MARKET)
    pool = Pool()
    market.fill_market(pool, tier)
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            elif event.type == QUIT: 
                return
        screen.blit(bg_surf, bg_rect)
        hangar.render()
        player_side.render()
        market.render()
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()