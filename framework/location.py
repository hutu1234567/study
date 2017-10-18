#_*_ coding:utf-8 _*_
class Point( object ):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x

    def setx(self, x): self.__x = x

    x = property( getx, setx )

    # Y property
    def gety(self): return self.__y

    def sety(self, y): self.__y = y

    y = property( gety, sety )

    def tuple(self):
        return (self.x, self.y)

class Size(object):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # X property
    def getwidth(self): return self.__width

    def setwidth(self, width): self.__width = width

    width = property( getwidth, setwidth )

    # Y property
    def getheight(self): return self.__height

    def setheight(self, height): self.__height = height

    height = property( getheight, setheight )