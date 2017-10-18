#_*_ coding:utf-8 _*_
import sys, random, math, pygame
from pygame.locals import *
#import common
from game.superman.gameobject import *


def start():

    pygame.init()
    screen = pygame.display.set_mode( (10240, 768) )
    pygame.display.set_caption( "斯古大陆" )

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        # fontobject = pygame.font.Font( None, 18 )

        pygame.draw.rect( screen, (0, 0, 0),
                          ((screen.get_width() / 2) - 100,
                           (screen.get_height() / 2) - 10,
                           200, 20), 0 )
        pygame.draw.rect( screen, (255, 255, 255),
                          ((screen.get_width() / 2) - 102,
                           (screen.get_height() / 2) - 12,
                           204, 24), 1 )
        pygame.display.update()