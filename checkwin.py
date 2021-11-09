#win-codes:   0:nothing  1:forced  2:victory

#forced = np.array([-1,-1])

def run(board, a, b):
    a = 6-a
    b -=1
    win = 0 #default state
    if a<=2:
        win = vertical(board,a,b)
    if win<1:
        win += horizontal(board,a,b)
    if not win:
        win += firstdiagonal(board,a,b)
    if not win:
        win += seconddiagonal(board,a,b)
    if win==0:
        print("Uh oh, looks like the match isn't over yet")
    elif win==1:
        print("HAha you gotta move it or you'll lose")
    elif win>1:
        print('I win! You suck!')
    else:
        print('Error: no matching win-code')

def vertical(board, a, b):
    i = 1
    while i<4 and board[a,b]==board[a+i,b]:
        i+=1
    if i==4:
        return 2
    elif i==3:
        forced = np.array([a+3,b])
        return 1   #forced move for the opponent
    return np.array([0])

def horizontal(board, a, b):
    i = 1
    while b-i>=0 and board[a,b]==board[a,b-i]:
        i+=1
    b-=i-1
    while b+i<7 and board[a,b]==board[a,b+i]:
        i+=1
    
    if i>=4:
        return 2
    #This one checks if it's forced win or if the opponent has only one (forced) move that doesn't lose
    #left_space = level[b-1]==(6-a-1) checks if the space on the left is free for a combination
    #right_space = level[b+3]==(6-a-1) same but on the right 
    # an example:
    #            |_|_|_|_|_|_|_| this is a forced win,       |_|_|_|_|_|_|_| here the opponent 
    #            |_|_|X|X|X|_|_| because the opponent (O)    |_|_|X|X|X|_|_| (O) has only one move
    #            |_|O|O|X|O|O|_| can't stop the sequence.    |_|X|O|O|X|_|_| that doesn't lose
    elif i==3:
        if b==0:
            if level[b+3]==(6-a-1):
                return 1
        elif b==4:
            if level[b-1]==(6-a-1):
                return 1
        else:
            left_space = level[b-1]==(6-a-1)
            right_space = level[b+3]==(6-a-1)
            if   left_space and right_space:
                return 2
            elif left_space or right_space:
                return 1
    #elif i==2:
    #    if b>1 and matrix[a,b-2]==1:
    else:
        return 0

def firstdiagonal(board, a, b):
    #top-left to bottom-right
    i = 1
    while a-i>=0 and b-i>=0 and board[a,b]==board[a-i,b-i]:
        i+=1
    a-=i-1
    b-=i-1
    while a+i<6 and b+i<7 and board[a,b]==board[a+i,b+i]:
        i+=1
    
    if i>=4:
        return 2
    if i==3 and b!=(0 or 4) and a!=(0 or 3) and level[b-1]==(6-a) and level[b+3]==(2-a):
        return 2
    return 0

def seconddiagonal(board, a, b):
    #bottom-left to top-right
    i = 1
    while a+i<6 and b-i>=0 and board[a,b]==board[a+i,b-i]:
        i+=1
    a+=i-1
    b-=i-1
    while a-i>=0 and b+i<7 and board[a,b]==board[a-i,b+i]:
        i+=1
    
    if i>=4:
        return 2
    if i==3 and b!=(0 or 4) and a!=(2 or 5) and level[b-1]==(4-a) and level[b+3]==(8-a):
        return 2
    return 0

import numpy as np

from util import issymmetrical
#pieces per column
#levels = numpy.zeros(7, numpy.int8)
level = np.array([0,0,0,2,3,4,4])

if __name__=='__main__':
    import util

    matrix = np.array([
        [0,0,0,0,0,0,0],
        [0,0,1,0,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0],
        [2,0,0,0,0,0,2],
        [0,0,0,0,0,0,0]])
    
    run(matrix,1,3)