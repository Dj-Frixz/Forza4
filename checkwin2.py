#win-codes:   0:nothing  1:forced  2:victory

import numpy as np

def run(board, empty_cells, b):
    a = empty_cells[b]
    win = np.array([0,0]) #default state: nothing found
    #vertical win check
    if a<3 and np.array_equal(board[a:a+4,b],np.full(4,1)):
        win[0] = 2
    #vertical tris check
    elif a==3:
        win[0] += np.array_equal(board[a:a+3,b],np.full(3,1))
        if win[0]==1:
            win[1] = b
    #horizontal win/tris check
    if win[0]!=2:
        win += horizontal(board[a],a,empty_cells==a+1)
    #top-left to bottom-right diagonal win/tris check
    if win[0]!=2:
        win += firstDiagonal(np.diagonal(board,b-a),b-a,empty_cells)
    #top-right to bottom-left diagonal win/tris check
    if win[0]!=2:
        win += secondDiagonal(np.diagonal(board[:,::-1],6-a-b)[::-1],6-a-b,empty_cells)
    if win[0]==0:
        return -1       #nothing
    elif win[0]==1:
        return win[1]   #forced move position
    else:
        return -2       #victory

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
            #two possible combinations, opponent already lost   ex. ||O|O|O||
            comb2 = np.where(e1*p2*p3*p4*np.append(e4[1:],False))[0] #01110
            if comb2.size:
                return 2
            else:
                return [1,comb[0]+3] #forced move
        else:
            comb = np.where(e1*p2*p3*p4)[0] #0111
            if comb.size:
                return [1,comb[0]]
            comb = np.where(p1*e2*p3*p4)[0] #1011
            if comb.size:
                return [1,comb[0]+1]
            comb = np.where(p1*p2*e3*p4)[0] #1101
            if comb.size:
                return [1,comb[0]+2]
    #no combination found
    return 0

def firstDiagonal(diagonal, offset, empty_cells):
    
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
        comb2 = np.where(e1*p2*p3*p4)[0] #0111
        if comb2.size:
            return 2 #01110
        else:
            return [1,comb[0]+3+b] #forced move
    else:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return [1,comb[0]+b]
        comb = np.where(p1*e2*p3*p4)[0] #1011
        if comb.size:
            return [1,comb[0]+1+b]
        comb = np.where(p1*p2*e3*p4)[0] #1101
        if comb.size:
            return [1,comb[0]+2+b]
    return 0

def secondDiagonal(diagonal, offset, empty_cells):
    
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
        comb2 = np.where(e1*p2*p3*p4)[0] #0111
        if comb2.size:
            return 2 #01110
        else:
            return [1,comb[0]+3+b] #forced move
    else:
        comb = np.where(e1*p2*p3*p4)[0] #0111
        if comb.size:
            return [1,comb[0]+b]
        comb = np.where(p1*e2*p3*p4)[0] #1011
        if comb.size:
            return [1,comb[0]+1+b]
        comb = np.where(p1*p2*e3*p4)[0] #1101
        if comb.size:
            return [1,comb[0]+2+b]
    return 0

if __name__=='__main__':
    matrix = np.array([
        [2,0,1,1,2,1,2],
        [1,0,1,2,1,2,1],
        [1,2,2,1,1,2,1],
        [2,2,1,2,2,2,2],
        [1,1,1,2,1,2,2],
        [2,2,1,1,2,1,1]])

    a,b = 0,0
    empty_cells = np.array([0,2,0,0,0,0,0])
    print(run(matrix==2,empty_cells,b))