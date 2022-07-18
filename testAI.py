import numpy as np
from time import perf_counter
import AI,AI2,AI3,AI4

if __name__=='__main__':

    board = np.array([
       #0 1 2 3 4 5 6
        0,0,0,0,0,0,0,
        1,2,0,0,0,0,0,
        2,1,2,2,0,1,2,
        2,1,1,1,2,2,1,
        1,1,2,1,1,1,2,
        1,2,1,2,1,2,1],np.int8).reshape((6,7))

    empty_cells = np.array([1,1,2,2,3,2,2],np.int8)

    timer = np.zeros(2)

    timer[0] = perf_counter()
    print(AI4.brain(board,empty_cells,1))
    timer[1] = perf_counter()
    #print(AI4.brain(board,empty_cells,2))
    #timer[2] = perf_counter()
    #print(AI3.brain(board,empty_cells,1))
    #timer[3] = perf_counter()

    print(np.diff(timer))