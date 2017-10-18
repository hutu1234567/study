#_*_ coding:utf-8 _*_
from framework.module import GameObject
import math
from framework.location import *
import pygame
from framework.module import font_path

class Planet(GameObject):
    def __init__(self):
        self = GameObject.__init__(self,image="earth.png")
        print("planet start!!")

    def draw(self,screen):
        width, height = self.getSize()
        #screen.blit(  self.getPos().tuple() )
        screen.blit( self.getLook(), (400 - width / 2, 300 - height / 2) )

class Space(GameObject):
    def __init__(self):
        self = GameObject.__init__(self,image="space.png")
        print("space start!!")


class SuperMan(GameObject):

    def wrap_angle(self,angle):
        return angle % 360


    def __init__(self):
        self.__angle = 0.0
        GameObject.__init__(self,image="superman.png")


        print("superman start!!")

    def draw(self,screen):
        width, height = self.getSize()
        pos = Point( 0, 0 )
        radius = 250

        self.__angle = self.wrap_angle( self.__angle - 0.1 )
        pos.x = math.sin( math.radians( self.__angle ) ) * radius
        pos.y = math.cos( math.radians( self.__angle ) ) * radius
        #screen.blit(  self.getPos().tuple() )
        screen.blit( self.getLook(), (400 + pos.x - width // 2, 300 + pos.y - height // 2) )

class Talking(GameObject):
    def draw(self,screen):
        pygame.draw.rect( screen, (0, 0, 0),
                          ((screen.get_width() / 2) - 100,
                           (screen.get_height() / 2) - 10,
                           200, 20), 0 )
        pygame.draw.rect( screen, (255, 255, 255),
                          ((screen.get_width() / 2) - 102,
                           (screen.get_height() / 2) - 12,
                           204, 24), 1 )
        fontobject = pygame.font.Font(font_path+"msyh.ttc", 28 )
        screen.blit( fontobject.render( "im superman!!我是超人", 1, (255, 255, 255) ),
                     ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10) )
if __name__ == '__main__':
    go = Space()