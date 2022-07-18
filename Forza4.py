import numpy as np
from numpy.core.fromnumeric import size
import checkwin2
import lib.pygame as pygame
from data.utils import load_sprite

class Game:

    def __init__(self):
        self.screen = None
        self._init_pygame()
        self.background = load_sprite('board.png',False)
        self.board = np.zeros((6,7),np.int8)
        self.disks = (load_sprite('disk2.png'),load_sprite('disk1.png'))
        self.grid = (
            pygame.Rect(163,87,58,420),
            pygame.Rect(233,87,58,420),
            pygame.Rect(300,87,58,420),
            pygame.Rect(368,87,58,420),
            pygame.Rect(436,87,58,420),
            pygame.Rect(503,87,58,420),
            pygame.Rect(570,87,58,420)
        )
        self.clock = pygame.time.Clock()
        self.empty_cells = np.full(7,6,np.int8)
        self.turn = 1
        self.last_move = 0

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Smart AI")
        pygame.display.set_icon(load_sprite('icon.png'))

    def play(self,mode):
        self._draw_init()
        if mode=='vsAI':
            self.vsAI()
        elif mode=='PvP':
            b = self._handle_input()
            self._draw(self.disks[self.turn%2],b)
            self._move(b)
            while checkwin2.run(self.board==self.turn%2+1,self.empty_cells,self.last_move)!=-2:
                b = self._handle_input()
                self._draw(self.disks[self.turn%2],b)
                self._move(b)
            print(f"Congratulations player {self.turn%2+1}, you won!\n")
        self._handle_input(end=1)

    def _handle_input(self,end=0):
        #waiting for user input
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and end==0:
                    mouse_pos = pygame.mouse.get_pos()
                    for i in range(7):
                        if self.grid[i].collidepoint(mouse_pos):
                            if self.empty_cells[i]!=0:
                                return i

    def _draw_init(self):
        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

    def _draw(self,surface,b):
        self.screen.blit(surface,(
            x.grid[b][0],73*self.empty_cells[b]+15
        ))
        pygame.display.flip()

    def _move(self,b):
        self.empty_cells[b] -= 1
        self.turn+=1
        self.board[ self.empty_cells[b], b ] = self.turn%2+1
        self.last_move = b

    def _PvP(self):
        pass

    def _vsAI(self,AI):
        pass

    def _reset(self):
        self.board = np.zeros((6,7),np.int8)
        self.empty_cells = np.full(7,6,np.int8)
        self.turn = 1

x = Game()
x.play('PvP')