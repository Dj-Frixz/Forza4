import numpy as np
import multiprocessing
import checkwin2
from data.utils import isSymmetrical

stop = 0

def moves(board,empty_cells,b,color):
    for x in b:
        new_board = board.copy()
        new_empties = empty_cells.copy()
        new_empties[x] -= 1
        new_board[ new_empties[x], x ] = color
        yield new_board
        yield new_empties

def checkwins(board,empty_cells,indices,color):
    victory = -1
    for i in indices:
        moved = move(board,empty_cells,i,color)
        if checkwin2.run(moved[0]==color,moved[1],i)==-2:
            if victory!=-1:
                return -2
            victory = i
    return victory

def brain(board,empty_cells,color):
    stop = empty_cells
    deepness = 1
    simm = isSymmetrical(board)

    if simm==1:
        indices = np.where(empty_cells[:4]!=0)[0]
        move = moves(board,empty_cells,indices,color)
        choices = np.zeros(indices.size,np.int8)
        for i in range(0,indices.size):
            choices[i] = checkwin2.run(next(move)==color,next(move)[1],indices[i])
            if choices[i]==-2: return i
        victory = checkwins(board,empty_cells,indices,(color%2)+1)
        if victory==-2:
            return -1
        if victory!=-1:
            return victory
        move = moves(board,empty_cells,indices,color)
        for i in range(0,indices.size):
            choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
    else:
        indices = np.where(empty_cells!=0)[0]
        move = moves(board,empty_cells,indices,color)
        choices = np.zeros(indices.size,np.int8)
        for i in range(0,indices.size):
            choices[i] = checkwin2.run(next(move)==color,next(move),indices[i])
            if choices[i]==-2: return i
        victory = checkwins(board,empty_cells,indices,(color%2)+1)
        if victory==-2:
            return -1
        if victory!=-1:
            return victory
        move = moves(board,empty_cells,indices,color)
        if simm==0:
            for i in range(0,indices.size):
                choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
        else:
            for i in indices:
                choices[i] = concentrate(next(move),next(move),(color%2)+1,deepness+1,choices[i])
    return choices

def think(board,empty_cells,color,deepness,forced=-1):
    simm = isSymmetrical(board)
    if simm==1:
        indices = np.where(empty_cells[:4]!=0)[0]
        move = moves(board,empty_cells,indices,color)
        choices = np.zeros(indices.size,np.int8)
        for i in range(0,indices.size):
            choices[i] = checkwin2.run(next(move)==color,next(move),indices[i])
            if choices[i]==-2: return (-1)**(color+1)
        if forced!=-1:
            move = moves(board,empty_cells,[forced],color)
            return think(next(move),next(move),(color%2)+1,deepness+1)
        move = moves(board,empty_cells,indices,color)
        for i in range(0,choices.size):
            choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
        if color%2:
            return np.amax(choices)
        else:
            return np.amin(choices)
    else:
        indices = np.where(empty_cells!=0)[0]
        move = moves(board,empty_cells,indices,color)
        choices = np.zeros(indices.size,np.int8)
        for i in range(0,indices.size):
            choices[i] = checkwin2.run(next(move)==color,next(move),indices[i])
            if choices[i]==-2: return (-1)**(color+1)
        if forced!=-1:
            move = moves(board,empty_cells,[forced],color)
            return think(next(move),next(move),(color%2)+1,deepness+1)
        move = moves(board,empty_cells,indices,color)
        if simm==0:
            for i in range(0,choices.size):
                choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
        else:
            for i in range(0,choices.size):
                choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
        if color%2:
            return np.amax(choices)
        else:
            return np.amin(choices)

def concentrate(board,empty_cells,color,deepness,forced=-1):
    indices = np.where(empty_cells!=0)[0]
    if indices.size==0:
        return 0
    move = moves(board,empty_cells,indices,color)
    choices = np.zeros(indices.size,np.int8)
    for i in range(0,indices.size):
        choices[i] = checkwin2.run(next(move)==color,next(move),indices[i])
        if choices[i]==-2: return (-1)**(color+1)
    if forced!=-1:
        move = moves(board,empty_cells,[forced],color)
        return concentrate(next(move),next(move),(color%2)+1,deepness+1)
    move = moves(board,empty_cells,indices,color)
    for i in range(0,choices.size):
        choices[i] = think(next(move),next(move),(color%2)+1,deepness+1,choices[i])
    if color%2:
        return np.amax(choices)
    else:
        return np.amin(choices)