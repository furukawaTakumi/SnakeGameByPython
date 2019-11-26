
import pyxel
from .ParcelState import ParcelState

class Field:
    def __init__(self, size):
        self.__size = size # (行,列)

    @property
    def size(self):
        return self.__size

    def Draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.__size[0]*8, self.__size[1]*8)
