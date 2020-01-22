try:
    import sys
    import collections
    import random
    import math
    import os
    import getopt
    import pygame
    from constants import *
    from pygame.locals import *
    from ship import *
except(ImportError, err):
    print('Failed to load module: %s' % (err))
    sys.exit(2)

class Pool():
    def __init__(self):
        self.n_ships = sum([a*b for a, b in list(zip([len(_) for _ in SHIPS], N_SHIPS_PER_TIER))])
        self.remaining = [set() for _ in range(len(N_SHIPS_PER_TIER))]
        self.pool_dict = collections.defaultdict()
        i = 0
        for tier, names in enumerate(SHIPS):
            for s in names:
                for j in range(N_SHIPS_PER_TIER[tier]):
                    self.pool_dict[i + j] = Ship(s)
                    self.remaining[tier].add(i + j)
                    i += 1
        for i in range(1, len(self.remaining)):
            self.remaining[i] = self.remaining[i].union(self.remaining[i - 1])



    def get_ships(self, tier):
        res = set(random.sample(self.remaining[tier], N_SHIPS_IN_MARKET_PER_TIER[tier]))
        for t in range(tier + 1):
            self.remaining[t] = self.remaining[t] - res
        return list(res)
