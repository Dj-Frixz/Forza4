import numpy

def issymmetrical(matrix):
    a = numpy.rot90(matrix)
    if numpy.equal(a[:3], numpy.flip(a[4:],1)):
        return 1    #it's symmetrical
    elif :
        return 0    #could be symmetrical in the future
    else:
        return -1   #not symmetrical