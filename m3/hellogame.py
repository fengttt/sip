# -*- coding: utf-8 -*-

import pygame, sys

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Frame Per Second
FPS = 60

if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    surf = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hello PyGame")

    while True:
        surf.fill(WHITE)
        pygame.draw.circle(surf, BLUE, (100, 100), 20)
        pygame.draw.circle(surf, BLUE, (100, 400), 20, 4)
        pygame.draw.rect(surf, RED, (400, 100, 20, 20))
        pygame.draw.rect(surf, RED, (400, 400, 20, 20), 4)
    
        for ev in pygame.event.get():
            if ev.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)        