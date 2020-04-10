# -*- coding: utf-8 -*-

import pygame, sys
import pygame.locals as pgl
import siplib.sg as sg

FPS = 60
fpsClock = pygame.time.Clock()

class GameState:
    def __init__(self, npixel):
        self.boardSz = 10
        self.blockSz = npixel // 10
        self.frameCnt = 0
        self.done = False
        self.blocks = [[sg.WHITE for i in range(self.boardSz)] 
                       for j in range(self.boardSz)]
        
    def colorBlocks(self, n):
        if n > self.boardSz:
            return
        for x in range(n):
            for y in range(n):
                self.blocks[x][y] = sg.BLUE
        for i in range(n):
            self.blocks[i][n-1] = sg.RED
            self.blocks[n-1][i] = sg.RED
            
    def draw(self, surf):
        for x in range(self.boardSz):
            for y in range(self.boardSz):
                pygame.draw.rect(surf, self.blocks[x][y],
                                 (x * self.blockSz,
                                  y * self.blockSz,
                                  self.blockSz, self.blockSz))
        for x in range(self.boardSz):
            pygame.draw.line(surf, sg.BLACK, 
                             (0, x*self.blockSz), 
                             (self.blockSz*self.boardSz, x*self.blockSz),
                             2)
            pygame.draw.line(surf, sg.BLACK,
                             (x*self.blockSz, 0),
                             (x*self.blockSz, self.boardSz * self.blockSz),
                             2)
            
def initState():
    return GameState(600)

def runOneFrame(surf, state):
    for ev in pygame.event.get():
        if ev.type == pgl.QUIT:
            state.done = True
    state.frameCnt += 1
    
    surf.fill(sg.WHITE)
    n = state.frameCnt // (FPS * 5)
    state.colorBlocks(n)
    state.draw(surf)
    if n > 0 and n < state.boardSz:
        msg = "Iteration {0}: Adding {1} red squares.".format(n, n*2-1)
        txtObj = sg.drawSmallText(msg, sg.BLACK, sg.WHITE)
        txtRect = txtObj.get_rect()
        txtRect.topleft = (10, 610)
        surf.blit(txtObj, txtRect)
        
if __name__ == '__main__':
    pygame.init()
    surf = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Hello PyGame")
    sg.initFc()
    state = initState()    
    while True:
        if state.done:
            pygame.quit()
            sys.exit()
        runOneFrame(surf, state)
        pygame.display.update()
        fpsClock.tick(FPS)
        