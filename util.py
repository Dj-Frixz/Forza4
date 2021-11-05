import numpy

def issymmetrical(matrix):
    rotmatrix = numpy.rot90(matrix)
    sidea = rotmatrix[:3]
    sidebflipped = numpy.flip(rotmatrix[4:],1)
    if numpy.equal(sidea, sidebflipped):
        return 1    #it's symmetrical
    elif sidea+sidebflipped:
        return 0    #could be symmetrical in the future
    else:
        return -1   #not symmetrical