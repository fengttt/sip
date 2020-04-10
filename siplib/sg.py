#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 10:37:53 2020

@author: ftian
"""

import pygame

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
GRAY = pygame.Color(128, 128, 128)
SILVER = pygame.Color(192, 192, 192)

def drawText(s, sz, c1, c2):
    fontObj = pygame.font.Font('freesansbold.ttf', sz)
    textObj = fontObj.render(s, True, c1, c2)
    return textObj

fontCache = [None, None, None]

def initFc():
    global fontCache
    fontCache[0] = pygame.font.Font('freesansbold.ttf', 16)
    fontCache[1] = pygame.font.Font('freesansbold.ttf', 24)
    fontCache[2] = pygame.font.Font('freesansbold.ttf', 32)

def drawSmallText(s, c1, c2):
    return fontCache[0].render(s, True, c1, c2)

def drawMidText(s, c1, c2):
    return fontCache[1].render(s, True, c1, c2)

def drawBigText(s, c1, c2):
    return fontCache[2].render(s, True, c1, c2)