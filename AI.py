import numpy as np
import concurrent.futures
import checkwin2
from data.utils import isSymmetrical

def checkwins(board,empty_cells,color):
    victory = -1
    if empty_cells[0]!=0:
        moved = move(board,empty_cells,0,color)
        if checkwin2.run(moved[0]==color,moved[1],0)==-2:
            victory = 0
    if empty_cells[1]!=0:
        moved = move(board,empty_cells,1,color)
        if checkwin2.run(moved[0]==color,moved[1],1)==-2:
            if victory!=-1:
                return -2
            victory = 1
    if empty_cells[2]!=0:
        moved = move(board,empty_cells,2,color)
        if checkwin2.run(moved[0]==color,moved[1],2)==-2:
            if victory!=-1:
                return -2
            victory = 2
    if empty_cells[3]!=0:
        moved = move(board,empty_cells,3,color)
        if checkwin2.run(moved[0]==color,moved[1],3)==-2:
            if victory!=-1:
                return -2
            victory = 3
    if empty_cells[4]!=0:
        moved = move(board,empty_cells,4,color)
        if checkwin2.run(moved[0]==color,moved[1],4)==-2:
            if victory!=-1:
                return -2
            victory = 4
    if empty_cells[5]!=0:
        moved = move(board,empty_cells,5,color)
        if checkwin2.run(moved[0]==color,moved[1],5)==-2:
            if victory!=-1:
                return -2
            victory = 5
    if empty_cells[6]!=0:
        moved = move(board,empty_cells,6,color)
        if checkwin2.run(moved[0]==color,moved[1],6)==-2:
            if victory!=-1:
                return -2
            victory = 6
    return victory

def brain(board,empty_cells,color):
    deepness = 1
    simm = isSymmetrical(board)
    choices = [None,None,None,None,None,None,None]
    
    if simm==1:
        win = -1
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            win = checkwin2.run(moved[0]==color,moved[1],3)
            if win==-2: return 3
        else: choices[3] = 10*(-1**(color%2))
        victory = checkwins(board,empty_cells,(color%2)+1)
        if victory==-2:
            return -1
        if victory!=-1:
            return victory
        with concurrent.futures.ProcessPoolExecutor() as executor:
            if empty_cells[0]!=0:
                moved = move(board,empty_cells,0,color)
                choices[0] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],0))
                choices[6] = choices[0]
            else: choices[0] = 10*(-1**(color%2))
            if empty_cells[1]!=0:
                moved = move(board,empty_cells,1,color)
                choices[1] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],1))
                choices[5] = choices[1]
            else: choices[1] = 10*(-1**(color%2))
            if empty_cells[2]!=0:
                moved = move(board,empty_cells,2,color)
                choices[2] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],2))
                choices[4] = choices[2]
            else: choices[2] = 10*(-1**(color%2))
            if empty_cells[3]!=0 and win!=-2:
                moved = move(board,empty_cells,3,color)
                choices[3] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,win)
            return [p.result() for p in concurrent.futures.as_completed(choices)]
    elif simm==0:
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = checkwin2.run(moved[0]==color,moved[1],0)
            if choices[0]==-2: return 0
        else: choices[0] = 10*(-1**(color%2))
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = checkwin2.run(moved[0]==color,moved[1],1)
            if choices[1]==-2: return 1
        else: choices[1] = 10*(-1**(color%2))
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = checkwin2.run(moved[0]==color,moved[1],2)
            if choices[2]==-2: return 2
        else: choices[2] = 10*(-1**(color%2))
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = checkwin2.run(moved[0]==color,moved[1],3)
            if choices[3]==-2: return 3
        else: choices[3] = 10*(-1**(color%2))
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            choices[4] = checkwin2.run(moved[0]==color,moved[1],4)
            if choices[4]==-2: return 4
        else: choices[4] = 10*(-1**(color%2))
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            choices[5] = checkwin2.run(moved[0]==color,moved[1],5)
            if choices[5]==-2: return 5
        else: choices[5] = 10*(-1**(color%2))
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            choices[6] = checkwin2.run(moved[0]==color,moved[1],6)
            if choices[6]==-2: return 6
        else: choices[6] = 10*(-1**(color%2))
        victory = checkwins(board,empty_cells,(color%2)+1)
        if victory==-2:
            return -1
        if victory!=-1:
            return victory
        with concurrent.futures.ProcessPoolExecutor() as executor:
            if empty_cells[0]!=0:
                moved = move(board,empty_cells,0,color)
                choices[0] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[0])
            if empty_cells[1]!=0:
                moved = move(board,empty_cells,1,color)
                choices[1] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[1])
            if empty_cells[2]!=0:
                moved = move(board,empty_cells,2,color)
                choices[2] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[2])
            if empty_cells[3]!=0:
                moved = move(board,empty_cells,3,color)
                choices[3] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[3])
            if empty_cells[4]!=0:
                moved = move(board,empty_cells,4,color)
                choices[4] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[4])
            if empty_cells[5]!=0:
                moved = move(board,empty_cells,5,color)
                choices[5] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[5])
            if empty_cells[6]!=0:
                moved = move(board,empty_cells,6,color)
                choices[6] = executor.submit(think,moved[0],moved[1],(color%2)+1,deepness+1,choices[6])
            return [p.result() for p in concurrent.futures.as_completed(choices)]
    elif simm==-1:
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = checkwin2.run(moved[0]==color,moved[1],0)
            if choices[0]==-2: return 0
        else: choices[0] = 10*(-1**(color%2))
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = checkwin2.run(moved[0]==color,moved[1],1)
            if choices[1]==-2: return 1
        else: choices[1] = 10*(-1**(color%2))
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = checkwin2.run(moved[0]==color,moved[1],2)
            if choices[2]==-2: return 2
        else: choices[2] = 10*(-1**(color%2))
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = checkwin2.run(moved[0]==color,moved[1],3)
            if choices[3]==-2: return 3
        else: choices[3] = 10*(-1**(color%2))
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            choices[4] = checkwin2.run(moved[0]==color,moved[1],4)
            if choices[4]==-2: return 4
        else: choices[4] = 10*(-1**(color%2))
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            choices[5] = checkwin2.run(moved[0]==color,moved[1],5)
            if choices[5]==-2: return 5
        else: choices[5] = 10*(-1**(color%2))
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            choices[6] = checkwin2.run(moved[0]==color,moved[1],6)
            if choices[6]==-2: return 6
        else: choices[6] = 10*(-1**(color%2))
        victory = checkwins(board,empty_cells,(color%2)+1)
        if victory==-2:
            return -1
        if victory!=-1:
            return victory
        with concurrent.futures.ProcessPoolExecutor() as executor:
            if empty_cells[0]!=0:
                moved = move(board,empty_cells,0,color)
                choices[0] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[0])
            if empty_cells[1]!=0:
                moved = move(board,empty_cells,1,color)
                choices[1] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[1])
            if empty_cells[2]!=0:
                moved = move(board,empty_cells,2,color)
                choices[2] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[2])
            if empty_cells[3]!=0:
                moved = move(board,empty_cells,3,color)
                choices[3] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[3])
            if empty_cells[4]!=0:
                moved = move(board,empty_cells,4,color)
                choices[4] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[4])
            if empty_cells[5]!=0:
                moved = move(board,empty_cells,5,color)
                choices[5] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[5])
            if empty_cells[6]!=0:
                moved = move(board,empty_cells,6,color)
                choices[6] = executor.submit(concentrate,moved[0],moved[1],(color%2)+1,deepness+1,choices[6])
            return [p.result() for p in concurrent.futures.as_completed(choices)]

def think(board,empty_cells,color,deepness,forced=-1):
    simm = isSymmetrical(board)
    if simm==1:
        choices = np.zeros(4,np.int8)
        win = -1
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            win = checkwin2.run(moved[0]==color,moved[1],3)
            if win==-2:
                return (-1)**(color+1)
        if forced!=-1:
            moved = move(board,empty_cells,forced,color)
            return think(moved[0],moved[1],(color%2)+1,deepness+1)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = think(moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],0))
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = think(moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],1))
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = think(moved[0],moved[1],(color%2)+1,deepness+1,checkwin2.run(moved[0]==color,moved[1],2))
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = think(moved[0],moved[1],(color%2)+1,deepness+1,win)
        if color%2:
            return np.amax(choices)
        else:
            return np.amin(choices)
    elif simm==0:
        choices = np.zeros(7,np.int8)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = checkwin2.run(moved[0]==color,moved[1],0)
            if choices[0]==-2:
                return (-1)**(color+1)
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = checkwin2.run(moved[0]==color,moved[1],1)
            if choices[1]==-2:
                return (-1)**(color+1)
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = checkwin2.run(moved[0]==color,moved[1],2)
            if choices[2]==-2:
                return (-1)**(color+1)
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = checkwin2.run(moved[0]==color,moved[1],3)
            if choices[3]==-2:
                return (-1)**(color+1)
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            choices[4] = checkwin2.run(moved[0]==color,moved[1],4)
            if choices[4]==-2:
                return (-1)**(color+1)
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            choices[5] = checkwin2.run(moved[0]==color,moved[1],5)
            if choices[5]==-2:
                return (-1)**(color+1)
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            choices[6] = checkwin2.run(moved[0]==color,moved[1],6)
            if choices[6]==-2:
                return (-1)**(color+1)
        if forced!=-1:
            moved = move(board,empty_cells,forced,color)
            return think(moved[0],moved[1],(color%2)+1,deepness+1)
        if empty_cells[0]!=0:
            moved = move(board,empty_cells,0,color)
            choices[0] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[0])
        if empty_cells[1]!=0:
            moved = move(board,empty_cells,1,color)
            choices[1] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[1])
        if empty_cells[2]!=0:
            moved = move(board,empty_cells,2,color)
            choices[2] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[2])
        if empty_cells[3]!=0:
            moved = move(board,empty_cells,3,color)
            choices[3] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[3])
        if empty_cells[4]!=0:
            moved = move(board,empty_cells,4,color)
            choices[4] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[4])
        if empty_cells[5]!=0:
            moved = move(board,empty_cells,5,color)
            choices[5] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[5])
        if empty_cells[6]!=0:
            moved = move(board,empty_cells,6,color)
            choices[6] = think(moved[0],moved[1],(color%2)+1,deepness+1,choices[6])
        if color%2:
            return np.amax(choices)
        else:
            return np.amin(choices)
    else:
        return concentrate(board,empty_cells,color,deepness,forced)

def concentrate(board,empty_cells,color,deepness,forced=-1):
    choices = np.zeros(7,np.int8)
    if empty_cells[0]!=0:
        moved = move(board,empty_cells,0,color)
        choices[0] = checkwin2.run(moved[0]==color,moved[1],0)
        if choices[0]==-2:
            return (-1)**(color+1)
    if empty_cells[1]!=0:
        moved = move(board,empty_cells,1,color)
        choices[1] = checkwin2.run(moved[0]==color,moved[1],1)
        if choices[1]==-2:
            return (-1)**(color+1)
    if empty_cells[2]!=0:
        moved = move(board,empty_cells,2,color)
        choices[2] = checkwin2.run(moved[0]==color,moved[1],2)
        if choices[2]==-2:
            return (-1)**(color+1)
    if empty_cells[3]!=0:
        moved = move(board,empty_cells,3,color)
        choices[3] = checkwin2.run(moved[0]==color,moved[1],3)
        if choices[3]==-2:
            return (-1)**(color+1)
    if empty_cells[4]!=0:
        moved = move(board,empty_cells,4,color)
        choices[4] = checkwin2.run(moved[0]==color,moved[1],4)
        if choices[4]==-2:
            return (-1)**(color+1)
    if empty_cells[5]!=0:
        moved = move(board,empty_cells,5,color)
        choices[5] = checkwin2.run(moved[0]==color,moved[1],5)
        if choices[5]==-2:
            return (-1)**(color+1)
    if empty_cells[6]!=0:
        moved = move(board,empty_cells,6,color)
        choices[6] = checkwin2.run(moved[0]==color,moved[1],6)
        if choices[6]==-2:
            return (-1)**(color+1)
    if forced!=-1:
        moved = move(board,empty_cells,forced,color)
        return concentrate(moved[0],moved[1],(color%2)+1,deepness+1)
    if empty_cells[0]!=0:
        moved = move(board,empty_cells,0,color)
        choices[0] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[0])
    if empty_cells[1]!=0:
        moved = move(board,empty_cells,1,color)
        choices[1] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[1])
    if empty_cells[2]!=0:
        moved = move(board,empty_cells,2,color)
        choices[2] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[2])
    if empty_cells[3]!=0:
        moved = move(board,empty_cells,3,color)
        choices[3] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[3])
    if empty_cells[4]!=0:
        moved = move(board,empty_cells,4,color)
        choices[4] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[4])
    if empty_cells[5]!=0:
        moved = move(board,empty_cells,5,color)
        choices[5] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[5])
    if empty_cells[6]!=0:
        moved = move(board,empty_cells,6,color)
        choices[6] = concentrate(moved[0],moved[1],(color%2)+1,deepness+1,choices[6])
    if color%2:
        return np.amax(choices)
    else:
        return np.amin(choices)

def move(board,empty_cells,b,color):
    table = board.copy()
    empty_spaces = empty_cells.copy()
    empty_spaces[b] -= 1
    table[ empty_spaces[b], b ] = color
    return table,empty_spaces