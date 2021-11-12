import numpy as np
import checkwin2
from util import issymmetrical

def brain(board,empty_cells,color):
    pass

def think(board,empty_cells,b,color,deepness):
    simm = issymmetrical(board)
    if simm==1:
        #win = ? then check forced (not before checking wins)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            win = checkwin2.run(moved[0],moved[1],0)
            if win==-2:
                return (-1)**color
            if win>-1:
                return think(moved[0],moved[1],((color+1)%2)+1,deepness+1)
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            if checkwin2.run(moved[0],moved[1],1)==2:
                return (-1)**color
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            if checkwin2.run(moved[0],moved[1],2)==2:
                return (-1)**color
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            if checkwin2.run(moved[0],moved[1],3)==2:
                return (-1)**color
        choices = np.zeros(4,np.int8)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            win = checkwin2(moved[0],moved[1])
            choices[0] = think(moved[0],moved[1],((color+1)%2)+1,deepness+1)
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = think(moved[0],moved[1],((color+1)%2)+1,deepness+1)
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = think(moved[0],moved[1],((color+1)%2)+1,deepness+1)
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = think(moved[0],moved[1],((color+1)%2)+1,deepness+1)
        #choices = np.concatenate((half_choices,half_choices[2::-1]))
        if color%2:
            return np.amin(choices)
        else:
            return np.amax(choices)
    elif simm==0:
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            if checkwin2.run(moved[0],moved[1],0)==2:
                return (-1)**color
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            if checkwin2.run(moved[0],moved[1],1)==2:
                return (-1)**color
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            if checkwin2.run(moved[0],moved[1],2)==2:
                return (-1)**color
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            if checkwin2.run(moved[0],moved[1],3)==2:
                return (-1)**color
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            if checkwin2.run(moved[0],moved[1],4)==2:
                return (-1)**color
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            if checkwin2.run(moved[0],moved[1],5)==2:
                return (-1)**color
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            if checkwin2.run(moved[0],moved[1],6)==2:
                return (-1)**color
        choices = np.zeros(4,np.int8)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            choices[4] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            choices[5] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            choices[6] = think(moved[0],moved[1],((color+1)%2)+1,deepness)
        if color%2:
            return np.amin(choices)
        else:
            return np.amax(choices)
    elif simm==-1:
        return concentrate(board,empty_cells,color,deepness)

def concentrate(board,empty_cells,color,deepness):
    if empty_cells[0]!=0:
        moved = move(board,empty_cells,0,color)
        if checkwin2.run(moved[0],moved[1],0)==2:
            return (-1)**color
    if empty_cells[1]!=0:
        moved = move(board,empty_cells,1,color)
        if checkwin2.run(moved[0],moved[1],1)==2:
            return (-1)**color
    if empty_cells[2]!=0:
        moved = move(board,empty_cells,2,color)
        if checkwin2.run(moved[0],moved[1],2)==2:
            return (-1)**color
    if empty_cells[3]!=0:
        moved = move(board,empty_cells,3,color)
        if checkwin2.run(moved[0],moved[1],3)==2:
            return (-1)**color
    if empty_cells[4]!=0:
        moved = move(board,empty_cells,4,color)
        if checkwin2.run(moved[0],moved[1],4)==2:
            return (-1)**color
    if empty_cells[5]!=0:
        moved = move(board,empty_cells,5,color)
        if checkwin2.run(moved[0],moved[1],5)==2:
            return (-1)**color
    if empty_cells[6]!=0:
        moved = move(board,empty_cells,6,color)
        if checkwin2.run(moved[0],moved[1],6)==2:
            return (-1)**color
    choices = np.zeros(7,np.int8)
    if empty_cells[0]!=0:
        moved = move(board,empty_cells,0,color)
        choices[0] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[1]!=0:
        moved = move(board,empty_cells,1,color)
        choices[1] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[2]!=0:
        moved = move(board,empty_cells,2,color)
        choices[2] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[3]!=0:
        moved = move(board,empty_cells,3,color)
        choices[3] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[4]!=0:
        moved = move(board,empty_cells,4,color)
        choices[4] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[5]!=0:
        moved = move(board,empty_cells,5,color)
        choices[5] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if empty_cells[6]!=0:
        moved = move(board,empty_cells,6,color)
        choices[6] = concentrate(moved[0],moved[1],((color+1)%2)+1,deepness+1)
    if color%2:
        return np.amax(choices)
    else:
        return np.amin(choices)

def move(board,empty_cells,b,color):
    empty_cells[b] -= 1
    board[ empty_cells[b], b ] = color
    return board,empty_cells