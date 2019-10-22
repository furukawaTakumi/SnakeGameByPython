
import pyxel
from .BodyColor import BodyColor as bColor

class SnakeBody():
    """ col: 体の色を文字列で指定する str() """
    def __init__(self, pos, color):
        self.position = pos
        self.__color = color

        pass

    @property
    def color(self):
        return self.__color

    def Draw(self):
        if bColor.BLUE == self.__color:
            pyxel.blt(self.__pos["x"], self.__pos["y"], 0, 8, 0, 8, 8)
        elif bColor.YELLOW == self.__color:
            pyxel.blt(self.__pos["x"], self.__pos["y"], 0, 0, 0, 8, 8)
