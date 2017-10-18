import sys, random, math, pygame
from pygame.locals import *
import common
import game.inputGame as ig
from framework.module import *

imgpath = common.getPath()+ "/img/"

def wrap_angle(angle):
    return angle % 360

def start():

    radius = 250
    angle = 0.0
    pos = Point( 0, 0 )
    old_pos = Point( 0, 0 )

    pygame.init()
    screen = pygame.display.set_mode( (800, 600) )
    pygame.display.set_caption( "星空" )
    font = pygame.font.Font( None, 18 )

    space=GameObject("space.png")
    #space = pygame.image.load(imgpath+ "space.png" ).convert_alpha()

    planet = pygame.image.load(imgpath+ "earth.png" ).convert_alpha()
    superman = pygame.image.load(imgpath+ "superman.png" ).convert_alpha()
    width, height = superman.get_size()
    superman = pygame.transform.smoothscale( superman, (width // 2, height // 2) )

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        fontobject = pygame.font.Font( None, 18 )
        space.draw(screen)
        #screen.blit( space.getLook(), space.getPos().tuple() )

        angle = wrap_angle( angle - 0.1 )
        pos.x = math.sin( math.radians( angle ) ) * radius
        pos.y = math.cos( math.radians( angle ) ) * radius

        # 获取位图的宽和高
        width, height = planet.get_size()
        # 在屏幕的中间绘制地球
        screen.blit( planet, (400 - width / 2, 300 - height / 2) )
        width, height = superman.get_size()
        screen.blit( superman, (400 + pos.x - width // 2, 300 + pos.y - height // 2) )

        pygame.draw.rect( screen, (0, 0, 0),
                          ((screen.get_width() / 2) - 100,
                           (screen.get_height() / 2) - 10,
                           200, 20), 0 )
        pygame.draw.rect( screen, (255, 255, 255),
                          ((screen.get_width() / 2) - 102,
                           (screen.get_height() / 2) - 12,
                           204, 24), 1 )
        pygame.display.update()
if __name__ == '__main__':
    start()