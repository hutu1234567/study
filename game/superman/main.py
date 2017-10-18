import sys, random, math, pygame
from pygame.locals import *
#import common
from game.superman.gameobject import *

#imgpath = common.getPath()+ "/img/"

def wrap_angle(angle):
    return angle % 360

def start():

    pygame.init()
    screen = pygame.display.set_mode( (800, 600) )
    pygame.display.set_caption( "超人" )
    #font = pygame.font.Font( None, 18 )


    space = Space()
    planet = Planet()
    superman = SuperMan()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        space.draw(screen)
        planet.draw(screen)
        superman.draw(screen)

        Talking().draw(screen)
        pygame.display.update()
if __name__ == '__main__':
    start()