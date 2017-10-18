#_*_ coding:utf-8 _*_
import os
def getPath():
    return os.path.realpath(os.getcwd())

if __name__ == '__main__':
    a = getPath()
    print(a)