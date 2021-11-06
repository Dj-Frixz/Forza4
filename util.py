import numpy as np

def issymmetrical(matrix):
    sidea, x, sideb = np.hsplit(matrix,np.array([3,4])) #rotates the matrix so slicing is possible among rows
    sideb_flipped = np.fliplr(sideb) #flips on the horizontal axis (left and right) to match sidea
    sides_sum = sidea + sideb_flipped

    if np.amin(np.equal(sidea, sideb_flipped)):
        return 1    #it's symmetrical
    elif sides_sum[sides_sum==3].size==0:   #search for 3s, which can appear only if 2+1, in which case the board can't return symmetrical anymore
        return 0    #could be symmetrical in the future
    else:
        return -1   #not symmetrical