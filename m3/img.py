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

    pikachu = pygame.image.load('pikachu.jpg')
    pikachu = pygame.transform.scale(pikachu, (300, 300))
    eevee = pygame.image.load('eevee.png')
    eevee = pygame.transform.scale(eevee, (300, 300))

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        surf.fill(sg.WHITE)
        surf.blit(pikachu, (10, 10))
        surf.blit(eevee, (350, 10))
            
        pygame.display.update()
        fpsClock.tick(FPS)             
