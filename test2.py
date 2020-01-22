import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1200, 800))

modes = pygame.display.list_modes(16)
if not modes:
    print('16-bit not supported')
else:
    print('Found resolution: ', modes[0])

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((40, 40, 40))
clock = pygame.time.Clock()

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        screen.blit(background, (0, 0))
        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    main()