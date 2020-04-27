# -*- coding: utf-8 -*-

import pygame, pygame.locals, sys
import siplib.sg as sg
import math

# Frame Per Second
FPS = 60

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Hello PyGame")
    sg.initFc()
    
    frameCnt = 0
    mouseMsg = ""
    kbdMsg = ""
    
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif ev.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                btn = ""
                if ev.button == 1:
                    btn = "LEFT"
                elif ev.button == 2:
                    btn = "MIDDLE"
                elif ev.button == 3:
                    btn = "RIGHT"
                else:
                    btn = "SOME"
                mouseMsg = "{0} button is clicked.  Position ({1}, {2})".format(
                    btn, mx, my)

                keys = pygame.key.get_pressed()
                if keys[pygame.locals.K_LSHIFT]:
                    mouseMsg = mouseMsg + " LEFT_SHIFT "
                if keys[pygame.locals.K_SPACE]:
                    mouseMsg = mouseMsg + " SPACE "
            elif ev.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                ks = ""
                if keys[pygame.locals.K_UP]:
                    ks = ks + "UP "
                
                if keys[pygame.locals.K_DOWN]:
                    ks = ks + "DOWN "
                    
                if keys[pygame.locals.K_LEFT]:
                    ks = ks + "LEFT "
                
                if keys[pygame.locals.K_RIGHT]:
                    ks = ks + " RIGHT "
                    
                if keys[pygame.locals.K_RETURN]:
                    ks = ks + "RETURN "
                    
                if ks == "":
                    ks = "SOME KEY "
                kbdMsg = ks + "is/are pressed."
                
        surf.fill(sg.WHITE)
        magicColor = (frameCnt % 256, 255 - frameCnt % 256, 0)
        pygame.draw.circle(surf, magicColor, (400, 300), 50)
        
        theta = (math.pi / FPS) * frameCnt * 0.1
        r1 = 200
        earthx = 400 + int(r1 * math.cos(theta))
        earthy = 300 + int(r1 * math.sin(theta))
        pygame.draw.circle(surf, sg.BLUE, (earthx, earthy), 10)
        
        r2 = 50
        moonx = earthx + int(r2 * math.cos(theta * 12))
        moony = earthy + int(r2 * math.sin(theta * 12))
        
        pygame.draw.circle(surf, sg.BLACK, (moonx, moony), 5)
        # pygame.draw.circle(surf, sg.BLUE, (100, 400), 20, 4)
        # pygame.draw.rect(surf, sg.RED, (400, 100, 20, 20))
        # pygame.draw.rect(surf, sg.RED, (400, 400, 20, 20), 4)
        # pygame.draw.line(surf, sg.BLACK, (400, 0), (400, 400), 10)

        frameCnt += 1
        msg = "Hello world.  Time: {0}s.  Frame Count {1}".format(frameCnt//FPS, frameCnt)
        txtObj = sg.drawBigText(msg, sg.BLACK, sg.WHITE)
        txtRect = txtObj.get_rect()
        txtRect.topleft = (10, 610)
        surf.blit(txtObj, txtRect)
        
        mouseObj = sg.drawMidText(mouseMsg, sg.BLACK, sg.WHITE)
        mouseRect = mouseObj.get_rect()
        mouseRect.topleft = (10, 700)
        surf.blit(mouseObj, mouseRect)
        
        kbdObj = sg.drawMidText(kbdMsg, sg.BLACK, sg.WHITE)
        kbdRect = kbdObj.get_rect()
        kbdRect.topleft = (10, 750)
        surf.blit(kbdObj, kbdRect)
            
        pygame.display.update()
        fpsClock.tick(FPS)        
