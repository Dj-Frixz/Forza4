import numpy as np
from time import perf_counter
import multiprocessing
import AI,AI2,AI3

if __name__=='__main__':

    board = np.array([
        #0 1 2 3 4 5 6
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]],np.int8)

    empty_cells = np.array([6,6,6,6,6,6,6],np.int8)

    timer = np.zeros(4)

    timer[0] = perf_counter()
    print(AI.brain(board,empty_cells,1))
    timer[1] = perf_counter()
    #print(AI2.brain(board,empty_cells,1))
    #timer[2] = perf_counter()
    #print(AI3.brain(board,empty_cells,1))
    #timer[3] = perf_counter()

    print(np.diff(timer))