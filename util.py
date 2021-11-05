import numpy

def issymmetrical(matrix):
    rotmatrix = numpy.rot90(matrix) #rotates the matrix so slicing is possible among rows
    sidea = rotmatrix[:3]
    sideb_flipped = numpy.flip(rotmatrix[4:],0) #flips on the vertical axis (up and down) to match sidea
    sides_sum = sidea + sideb_flipped

    if numpy.amin(numpy.equal(sidea, sideb_flipped)):
        return 1    #it's symmetrical
    elif sides_sum[sides_sum==3].size==0:   #search for 3s, which can appear only if 2+1, in which case the board can't return symmetrical anymore
        return 0    #could be symmetrical in the future
    else:
        return -1   #not symmetrical