try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from constants import *
    from pygame.locals import *
    from util import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)

SHIPS = [
    ['ibis', 'bantam'],
    ['heron', 'kestrel', 'griffin', 'condor', 'cormorant'],
    ['merlin', 'corax'],
    ['osprey', 'blackbird', 'caracal', 'moa'],
    ['ferox', 'drake', 'naga'],
    ['scorpion', 'raven', 'rokh']
]

class Ship():
    def __init__(self, name):
        self.name = name
        self.tier = None
        self.attack = None
        self.attack_type = None
        self.shield = None
        self.armor = None
        self.hull = None
        self.race = None
        self.special = None
        self.surf, self.rect = load_png(self.name + '.png')
        self.surf = pygame.transform.scale(self.surf, SHIP_BLOCK_SIZE)
