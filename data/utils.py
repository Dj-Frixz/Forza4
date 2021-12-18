import numpy as np
from pygame.image import load

def isSymmetrical(matrix):
    #slice the matrix vertically
    sidea, x, sideb = np.hsplit(matrix,np.array([3,4]))
    #flip 'left and right' sideb to match sidea
    sideb_flipped = np.fliplr(sideb)

    if np.array_equal(sidea, sideb_flipped):
        return 1    #it's symmetrical
    else:
        sides_sum = sidea + sideb_flipped
        #search for 3s, which can only appear if '2+1', in which case the board can't return symmetrical anymore
        if np.array_equal(sides_sum[sides_sum==3],[]):
            return 0    #could be symmetrical in the future
        else:
            return -1   #not symmetrical

def load_sprite(name, withAlpha=True):
    path = f'data/sprites/{name}'
    loaded_sprite = load(path)

    if withAlpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()