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
HUMAN = 0
COMPUTER = 1

SERGEANT = 0
LIEUTENANT = 1
CAPTAIN = 2
MAJOR = 3
COLONEL = 4
GENERAL = 5

FITTING = 0
BATTLE = 1

SHIPYARD_PADDING_X = 50
SHIPYARD_PADDING_Y = 50
SHIPYARD_BLOCK_SIZE = 100

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
        if self.player == HUMAN:
            self.rect.midbottom = self.area.midbottom
        elif self.player == COMPUTER:
            self.rect.midtop = self.area.midtop

class Shipyard(pygame.sprite.Sprite):
    def __init__(self, rank):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('shipyard.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.move_ip(SHIPYARD_PADDING_X, SHIPYARD_PADDING_Y)
        self.rank = rank
        self.rows = 1
        self.cols = 4
        self.reinit()

    def reinit(self):
        if self.rank == GENERAL:
            self.rows = 3
            self.cols = 4

class Ship(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('armageddon.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.id = id
        self.attack = 3
        self.defense = 3
        self.attack_type = 1
        self.defense_type = 1
        self.evasion = 0.0
        self.hull = 3
        self.shipyard_loc = id
        self.player = HUMAN
        self.board_loc = 0
        self.update()

    def update(self):
        self.rect.left = SHIPYARD_PADDING_X + (self.shipyard_loc % 4)*SHIPYARD_BLOCK_SIZE
        self.rect.top = SHIPYARD_PADDING_Y + (self.shipyard_loc // 4)*SHIPYARD_BLOCK_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('S P A C E   A C E')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((40, 40, 40))

    global player1
    global player2
    player1 = Board(HUMAN)
    player2 = Board(COMPUTER)

    shipyard = Shipyard(GENERAL)

    ship = Ship(8)


    playersprite = pygame.sprite.RenderPlain(player1)
    complayersprite = pygame.sprite.RenderPlain(player2)
    shipyardsprite = pygame.sprite.RenderPlain(shipyard)
    shipsprites = pygame.sprite.RenderPlain(ship)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    phase = FITTING

    while 1:
        screen.blit(background, (0, 0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_1:
                    phase = FITTING
                if event.key == K_2:
                    phase = BATTLE

        

        if ship.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 0, 0), pygame.Rect(525, 50, 200, 300))

        if phase == FITTING:
            screen.blit(background, player1.rect, player1.rect)
            playersprite.update()
            playersprite.draw(screen)
            shipyardsprite.draw(screen)
            shipsprites.draw(screen)
        elif phase == BATTLE:
            screen.blit(background, player1.rect, player1.rect)
            screen.blit(background, player2.rect, player2.rect)
            playersprite.update()
            complayersprite.update()
            playersprite.draw(screen)
            complayersprite.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()