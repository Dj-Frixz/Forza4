import numpy as np
import checkwin2

class Game:

    def __init__(self):
        self.board = np.zeros((6,7),np.int8)
        self.empty_cells = np.full(7,6,np.int8)
        self.turn = 0
        self.last_move = 0
    
    def play(self,mode='vsAI',AI=1):
        if mode=='vsAI':
            if AI==2:

                self.vsAI(AI)
        elif mode=='PvP':
            for i in range(7):
                print('\n',self.board,'\n')
                self.move(int(input(f"Choose your column player {self.turn%2+1}: ")))
                self.turn += 1
            print('Check!')
            self.turn -= 1
            while checkwin2.run(self.board,self.empty_cells,self.last_move,self.turn%2+1)!=2:
                self.turn += 1
                print('\n',self.board,'\n')
                self.move(int(input(f"Choose your column player {self.turn%2+1}: ")))
            print('\n',self.board,'\n')
            print(f"Congratulations player {self.turn%2+1}, you won!\n")
        else:
            raise ValueError

    def move(self,b):
        self.empty_cells[b] -= 1
        self.board[ self.empty_cells[b], b ] = self.turn%2+1
        self.last_move = b

    def PvP(self):
        pass

    def vsAI(self,AI):
        pass

    def reset(self):
        self.board = np.zeros((6,7),np.int8)
        self.empty_cells = np.full(7,6,np.int8)
        self.turn = 1

x = Game()
x.play('PvP')