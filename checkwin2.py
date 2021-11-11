#win-codes:   0:nothing  1:forced  2:victory

import numpy as np

def run(board, empty_cells, b, player):
    a = empty_cells[b]
    win = 0 #default state: nothing found
    #vertical win check
    if a<3 and np.array_equal(board[a:a+4,b],np.full(4,1)):
        win = 2
    #vertical tris check
    elif a==3:
        win += np.array_equal(board[a:a+3,b],np.full(3,1))
    #horizontal win/tris check
    if win!=2:
        win += horizontal(board[a]==player,a,empty_cells==a+1)
    #top-left to bottom-right diagonal win/tris check
    if win!=2:
        win += firstdiagonal(np.diagonal(board,b-a)==player,b-a,empty_cells)
    #top-right to bottom-left diagonal win/tris check
    if win!=2:
        win += seconddiagonal(np.diagonal(board[:,::-1],6-a-b)[::-1] == player,6-a-b,empty_cells)
    if win==0:
        return 0    #nothing
    elif win==1:
        return 1    #forced move
    else:
        return 2    #victory

def horizontal(row, row_index, empty_cells):

    #points made
    p1 = row[:4]
    p2 = row[1:5]
    p3 = row[2:6]
    p4 = row[3:]

    #where 'four in a row'?
    comb = np.where(p1*p2*p3*p4)[0]         #1111

    #checks if '4 in a row' was found
    if comb.size:
        return 2 #victory
    else:
        #cells that could be filled
        e1 = empty_cells[:4]
        e2 = empty_cells[1:5]
        e3 = empty_cells[2:6]
        e4 = empty_cells[3:]
        
        comb = np.where(p1*p2*p3*e4)[0]     #1110

        if comb.size:
            #two possible combinations, opponent already lost   ex. |_|O|O|O|_|
            comb = np.where(e1*p2*p3*p4*np.append(e4[1:],False))[0] #01110
            if comb.size:
                return 2
            else:
                return 1 #forced move
        else:
            comb = np.where(e1*p2*p3*p4)[0] #0111
            if comb.size:
                return 1
            comb = np.where(p1*e2*p3*p4)[0] #1011
            if comb.size:
                return 1
            comb = np.where(p1*p2*e3*p4)[0] #1101
            if comb.size:
                return 1
    #no combination found
    return 0

def firstdiagonal(diagonal, offset, empty_cells):
    
    if diagonal.size<4:
        return 0
    
    if offset>0:
        a,b = 0,offset
        offset = 7
    else:
        a,b = -offset,0
        offset = offset+6

    p1 = diagonal[:-3]
    p2 = diagonal[1:-2]
    p3 = diagonal[2:-1]
    p4 = diagonal[3:]

    comb = np.where(p1*p2*p3*p4)[0]

    if comb.size:
        return 2
    
    empty_pos = np.arange(a+1,a+1+offset-b) == empty_cells[b:offset]
    e1 = empty_pos[:-3]
    e2 = empty_pos[1:-2]
    e3 = empty_pos[2:-1]
    e4 = empty_pos[3:]

    comb = np.where(p1*p2*p3*e4)[0]     #1110

    if comb.size:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return 2 #01110
        else:
            return 1 #forced move
    else:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return 1
        comb = np.where(p1*e2*p3*p4)[0] #1011
        if comb.size:
            return 1
        comb = np.where(p1*p2*e3*p4)[0] #1101
        if comb.size:
            return 1
    return 0

def seconddiagonal(diagonal, offset, empty_cells):
    
    if diagonal.size<4:
        return 0
    
    if offset>0:
        a,b = 6-offset,0
        offset = a+1
    else:
        a,b = 5,1-offset
        offset = a+2
    
    p1 = diagonal[:-3]
    p2 = diagonal[1:-2]
    p3 = diagonal[2:-1]
    p4 = diagonal[3:]

    comb = np.where(p1*p2*p3*p4)[0]

    if comb.size:
        return 2

    empty_pos = np.arange(a+1,a+1-offset+b,-1) == empty_cells[b:offset]
    e1 = empty_pos[:-3]
    e2 = empty_pos[1:-2]
    e3 = empty_pos[2:-1]
    e4 = empty_pos[3:]

    comb = np.where(p1*p2*p3*e4)[0]     #1110

    if comb.size:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return 2 #01110
        else:
            return 1 #forced move
    else:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return 1
        comb = np.where(p1*e2*p3*p4)[0] #1011
        if comb.size:
            return 1
        comb = np.where(p1*p2*e3*p4)[0] #1101
        if comb.size:
            return 1
    return 0

if __name__=='__main__':
    matrix = np.array([
            #0 1 2 3 4 5 6
            [0,0,0,0,0,0,0], #0
            [0,0,0,0,0,0,0], #1
            [0,0,0,0,0,0,0], #2
            [0,0,0,0,1,1,1], #3
            [0,2,0,2,0,2,0], #4
            [0,0,0,0,0,0,0]])#5

    a,b = 3,4
    empty_cells = np.array([6,6,6,4,3,3,3])
    run(matrix,empty_cells,a,b,1)
