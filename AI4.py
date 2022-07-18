import numpy as np
import multiprocessing
import checkwin4
from data.utils import isSymmetrical

def brain(board,empty_cells,color):
    deepness = 1
    simm = isSymmetrical(board)
    indices = np.where(empty_cells!=0)[0]

    for i in indices:
        moved = move(board,empty_cells,i,color)
        win = checkwin4.run(moved[0]==color,moved[1],i)
        if win==-2: return i
    victory = checkwins(board,empty_cells,indices,(color%2)+1)
    if victory==-2:
        return -1
    if victory!=-1:
        return victory

    if simm==1:
        indices = np.where(empty_cells[:4]!=0)[0]
        choices = np.zeros(indices.size,np.int8)
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = think(moved[0],moved[1],(color%2)+1,deepness+1,checkwin4.run(moved[0]==color,moved[1],i))
    elif simm==0:
        choices = np.zeros(indices.size,np.int8)
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = think(moved[0],moved[1],(color%2)+1,deepness+1,checkwin4.run(moved[0]==color,moved[1],i))
    else:
        choices = np.zeros(indices.size,np.int8)
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,checkwin4.run(moved[0]==color,moved[1],i))
    result = np.amax(choices) if color==1 else np.amin(choices)
    return np.random.default_rng().choice(np.where(choices==result))

def think(board,empty_cells,color,deepness,forced=-1):
    if np.array_equal(empty_cells,[0,0,0,0,0,0,0]):
        return 0
    simm = isSymmetrical(board)
    choices = np.zeros(7,np.int8)
    if simm==1:
        indices = np.where(empty_cells[:4]!=0)[0]
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = checkwin4.run(moved[0]==color,moved[1],i)
            if choices[i]==-2: return (-1)**(color+1)
        if forced!=-1:
            moved = move(board,empty_cells,forced,color)
            return think(moved[0],moved[1],(color%2)+1,deepness+1)
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[i])
    else:
        indices = np.where(empty_cells!=0)[0]
        for i in indices:
            moved = move(board,empty_cells,i,color)
            choices[i] = checkwin4.run(moved[0]==color,moved[1],i)
            if choices[i]==-2: return (-1)**(color+1)
        if forced!=-1:
            moved = move(board,empty_cells,forced,color)
            return think(moved[0],moved[1],(color%2)+1,deepness+1)
        if simm==0:
            for i in indices:
                moved = move(board,empty_cells,i,color)
                choices[i] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[i])
        else:
            for i in indices:
                moved = move(board,empty_cells,i,color)
                choices[i] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[i])
    if color%2:
        return np.amax(choices[indices])
    else:
        return np.amin(choices[indices])

def concentrate(board,empty_cells,color,deepness,forced=-1):
    indices = np.where(empty_cells!=0)[0]
    if indices.size==0:
        return 0
    choices = np.zeros(7,np.int8)
    for i in indices:
        moved = move(board,empty_cells,i,color)
        choices[i] = checkwin4.run(moved[0]==color,moved[1],i)
        if choices[i]==-2: return (-1)**(color+1)
    if forced!=-1:
        moved = move(board,empty_cells,forced,color)
        return concentrate(moved[0],moved[1],(color%2)+1,deepness+1)
    for i in indices:
                moved = move(board,empty_cells,i,color)
                choices[i] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,checkwin4.run(moved[0]==color,moved[1],i))
    if color%2:
        return np.amax(choices[indices])
    else:
        return np.amin(choices[indices])

def move(board,empty_cells,b,color):
    table = board.copy()
    empty_spaces = empty_cells.copy()
    empty_spaces[b] -= 1
    table[ empty_spaces[b], b ] = color
    return table,empty_spaces

def checkwins(board,empty_cells,indices,color):
    victory = -1
    for i in indices:
        moved = move(board,empty_cells,i,color)
        if checkwin4.run(moved[0]==color,moved[1],i)==-2:
            if victory!=-1:
                return -2
            victory = i
    return victory