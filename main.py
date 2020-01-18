#
# Space Ace
# Author: Tony Wong
#
# A space themed roguelike auto-battler. Pick your ships and strategically
# them to give your fleet the best odds of winning the fight.
#

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from pygame.locals import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def load_png(name):
    """
    Params: filename of image
    Returns: image object
    """
    fullname = os.path.join('data/images/', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except(pygame.error, message):
        print('Failed to load image: ', fullname)
        raise(SystemExit, message)
    return image, image.get_rect()

class Board(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('board.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.player = player
        self.reinit()

    def reinit(self):
        if self.player == 'human':
            self.rect.midbottom = self.area.midbottom
        elif self.player == 'computer':
            self.rect.midtop = self.area.midtop

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('S P A C E   A C E')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    global player1
    global player2
    player1 = Board('human')
    player2 = Board('computer')

    playersprites = pygame.sprite.RenderPlain((player1, player2))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        screen.blit(background, player1.rect, player1.rect)
        screen.blit(background, player2.rect, player2.rect)
        playersprites.update()
        playersprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()