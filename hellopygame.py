#_*_ coding:utf-8 _*_

import pygame
import sys
import math
from pygame.locals import *
import common

#if __name__ == '__main__':
pygame.init()
screen = pygame.display.set_mode( (600, 500) )
#myfont = pygame.font.Font( None, 60 )
white = 255,255,255
blue = 0,0,200
#textImage = myfont.render("Hello Pygame", True, white)

pygame.display.set_caption( "Drawing Rectangles" )
pos_x = 300
pos_y = 250
vel_x = 1
vel_y = 1
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill( blue )
    #screen.blit( textImage, (100, 100) )

    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle( screen, color, position, radius, width )

    # 移动矩形
    pos_x += vel_x
    pos_y += vel_y
    # 使矩形保持在窗口内
    if pos_x > 500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y > 400 or pos_y < 0:
        vel_y = -vel_y
    # 绘制矩形
    color = 255, 255, 0
    width = 0  # solid fill
    pos = pos_x, pos_y, 100, 100
    pygame.draw.rect( screen, color, pos, width )

    color = 255, 255, 0
    width = 8
    pygame.draw.line( screen, color, (100, 100), (500, 400), width )

    # 绘制弧形的代码
    color = 255, 0, 111
    position = 111, 150, 200, 200
    start_angle = math.radians( 0 )
    end_angle = math.radians( 222 )
    width = 3
    pygame.draw.arc( screen, color, position, start_angle, end_angle, width )
    imgpath = common.getPath() + "/img/"
    print(imgpath)
    img = pygame.image.load(imgpath+ "superman.png" ).convert_alpha()
    screen.blit( img, (0,0) )

    pygame.display.update()
