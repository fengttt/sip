# -*- coding: utf-8 -*-

import pygame, pygame.locals, sys, random
import siplib.sg as sg


FPS = 2 
N = 100
PIXEL = 600
HEAL_DAYS = 20
INFECT_RATE = 20 
N0 = 3


class Person:
    def __init__(self):
        self.infect_ts = -1
        self.heal_ts = -1 

    def infectAt(self, ts):
        self.infect_ts = ts
        self.heal_ts = ts + HEAL_DAYS 

    def infected(self):
        return self.infect_ts >= 0

    def sick(self, ts):
        return ts >= self.infect_ts and ts < self.heal_ts

    def color(self, ts):
        if not self.infected():
            return sg.WHITE
        elif self.sick(ts):
            return sg.RED
        else:
            return sg.PINK

class GameState:
    def __init__(self, n, pixel): 
        self.n = n
        self.sz = pixel // n
        self.persons = [Person() for i in range(n*n)]

    def draw(self, surf, ts):
        for x in range(self.n):
            for y in range(self.n):
                me = y * self.n + x
                pygame.draw.rect(surf, self.persons[me].color(ts),
                                 (x * self.sz, y * self.sz, self.sz, self.sz))

    def infectMe(self, ts, me, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:
            neighbour = y * self.n + x
            if self.persons[neighbour].sick(ts):
                if random.uniform(0, 100) < INFECT_RATE:
                    self.persons[me].infectAt(ts)
                    return True
        return False

    def update(self, ts):
        oldx = 0 
        inc = 0
        for x in range(self.n):
            for y in range(self.n):
                me = y * self.n + x
                if self.persons[me].infected():
                    oldx += 1
                    continue
                elif self.infectMe(ts, me, x-1, y):
                    inc += 1
                    continue
                elif self.infectMe(ts, me, x+1, y): 
                    inc += 1
                    continue
                elif self.infectMe(ts, me, x, y-1):
                    inc += 1
                    continue
                elif self.infectMe(ts, me, x, y+1):
                    inc += 1
                    continue
        return (oldx, inc) 

    def infectSome(self, n0):
        for i in range(n0):
            idx = random.randint(0, self.n * self.n - 1)
            self.persons[idx].infectAt(0)


            
def initState():
    return GameState(N, PIXEL) 

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((PIXEL, PIXEL + 200)) 
    pygame.display.set_caption("COVID-19 Spread")
    sg.initFc()
    state = initState()    
    state.infectSome(N0)

    frameCnt = 0
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        frameCnt += 1
        ts = frameCnt

        surf.fill(sg.WHITE)
        oldx, inc = state.update(ts)
        state.draw(surf, ts)

        msg = "At tick {0}s, total infected grow from {1} to {2}".format(ts, oldx, oldx + inc) 
        txtObj = sg.drawSmallText(msg, sg.BLACK, sg.WHITE)
        txtRect = txtObj.get_rect()
        txtRect.topleft = (10, 10 + PIXEL)
        surf.blit(txtObj, txtRect)
        pygame.display.update()
        fpsClock.tick(FPS)
        
