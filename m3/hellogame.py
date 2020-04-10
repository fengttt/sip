# -*- coding: utf-8 -*-

import pygame, pygame.locals, sys
import siplib.sg as sg

# Frame Per Second
FPS = 60

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Hello PyGame")
    sg.initFc()
    
    frameCnt = 0
    while True:
        # surf.fill(sg.WHITE)
        pygame.draw.circle(surf, sg.BLUE, (100+frameCnt, 100), 20)
        # pygame.draw.circle(surf, sg.BLUE, (100, 400), 20, 4)
        # pygame.draw.rect(surf, sg.RED, (400, 100, 20, 20))
        # pygame.draw.rect(surf, sg.RED, (400, 400, 20, 20), 4)
        
        frameCnt += 1
        msg = "Hello world.  Time: {0}s.  Frame Count {1}".format(frameCnt//FPS, frameCnt)
        txtObj = sg.drawSmallText(msg, sg.BLACK, sg.WHITE)
        txtRect = txtObj.get_rect()
        txtRect.topleft = (10, 610)
        surf.blit(txtObj, txtRect)
    
        for ev in pygame.event.get():
            if ev.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)        