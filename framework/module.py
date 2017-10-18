#_*_ coding:utf-8 _*_
import common as common
import pygame as pygame
from framework.location import *

img_path = common.getPath() + "/img/"
font_path = common.getPath() + "/font/"

class GameObject():
    __pos=Point(0,0)

    def getPos(self):
        return self.__pos

    def getLook(self):
        return self.__look

    def getSize(self):
        return self.__size

    def __init__(self, image = None, pos = None, size = None):
        if(image is not None):
            self.__look = pygame.image.load( img_path + image ).convert_alpha()
        else:
            self.__look = None
        if(pos is not None):
            self.__pos=pos
        if(size is not None):
            self.__size=size
        else:
            if(self.__look != None):
                self.__size=self.__look.get_size()

        print("size===")

    def draw(self,screen):
        screen.blit( self.getLook(), self.getPos().tuple() )
if __name__ == '__main__':
    p=Point(2,3)
    print(p.x)
    p.x=4
    print(p.x)
    print(p.tuple())