def run(board, a, b):
    a = 6-a
    b -=1
    win = 0
    if a<=2:
        win = vertical(board, a, b)
    if not win:
        win = horizontal(board, a, b)
    """if not win:
        win = diagonal(board, a, b)"""
    if win:
        print('I win! You suck!')
    else:
        print("Uh oh, looks like the match isn't over yet")

def vertical(board, a, b):
    i = 1
    while i<4 and board[a][b]==board[a+i][b]:
        i+=1
                                                                                #3 CHECK to add!!!! (forced move for the opponent)
    if i==4:
        return 1
    return 0

def horizontal(board, a, b):
    i = 1
    while b-i>=0 and board[a][b]==board[a][b-i]:
        i+=1
    b-=i-1
    while b+i<7 and board[a][b]==board[a][b+i]:
        i+=1
    
    if i==4:
        return 1
    if i==3 and level[b-1]==level[b+i]==(6-a-1):
        return 1
    return 0

import numpy

#pieces per column
#levels = numpy.zeros(7, numpy.int8)
level = numpy.array([0,0,0,0,0,0,0])

matrix = numpy.array([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]])

run(matrix,2,4)