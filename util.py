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