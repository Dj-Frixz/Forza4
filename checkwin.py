def run(board, a, b):
    a = 6-a
    b -=1
    win = 0
    if a<=2:
        win = vertical(board, a, b)
    """if not win:
        win = horizontal(board, a, b)
    if not win:
        win = diagonal(board, a, b)"""
    if win:
        print('I win! You suck!')
    else:
        print("Uh oh, looks like the match isn't over yet")

def vertical(board, a, b):
    i = 1
    print(board[a][b])
    while i<4 and board[a][b]==board[a+i][b]:
        print(board[a+i][b])
        i+=1
    if i==4:
        return 1
    return 0

import numpy

matrix = numpy.array([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]])

run(matrix,4,4)