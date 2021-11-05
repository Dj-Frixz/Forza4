def run(board, a, b):
    a = 6-a
    b -=1
    win = 0
    if a<=2:
        win = vertical(board,a,b)
    if not win:
        win = horizontal(board,a,b)
    if not win:
        win = firstdiagonal(board,a,b)
    if not win:
        win = seconddiagonal(board,a,b)
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
    
    if i>=4:
        return 1
    if i==3 and b!=(0 or 4) and level[b-1]==level[b+3]==(6-a-1):
        return 1
    return 0

def firstdiagonal(board, a, b):
    #top-left to bottom-right
    i = 1
    while a-i>=0 and b-i>=0 and board[a][b]==board[a-i][b-i]:
        i+=1
    a-=i-1
    b-=i-1
    while a+i<6 and b+i<7 and board[a][b]==board[a+i][b+i]:
        i+=1
    
    if i>=4:
        return 1
    if i==3 and b!=(0 or 4) and a!=(0 or 3) and level[b-1]==(6-a) and level[b+3]==(2-a):
        return 1
    return 0

def seconddiagonal(board, a, b):
    #bottom-left to top-right
    i = 1
    while a+i<6 and b-i>=0 and board[a][b]==board[a+i][b-i]:
        i+=1
    a+=i-1
    b-=i-1
    while a-i>=0 and b+i<7 and board[a][b]==board[a-i][b+i]:
        i+=1
    
    if i>=4:
        return 1
    if i==3 and b!=(0 or 4) and a!=(2 or 5) and level[b-1]==(4-a) and level[b+3]==(8-a):
        return 1
    return 0

if __name__=='__main__':
    import numpy

    #pieces per column
    #levels = numpy.zeros(7, numpy.int8)
    level = numpy.array([0,0,0,2,3,4,4])

    matrix = numpy.array([
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,2,0,1,2],
        [0,0,0,0,1,0,2],
        [0,0,0,1,0,1,2],
        [0,0,0,0,0,0,1]])

    run(matrix,3,5)