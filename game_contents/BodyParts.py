
import pyxel
from .BodyColor import BodyColor as bColor


class BodyParts:
    def __init__(self, pos, color):
        self.position = pos
        self.__set_col(color)
        pass

    def Draw(self):
        pyxel.blt(self.position["x"], self.position["y"], self.__col_pos["x"], self.__col_pos["y"], 0, 8, 8,15)

    def __set_col(self, color):
        if bColor.BLUE == color:
            self.__col_pos = {"x": 8, "y":0 }
        elif bColor.YELLOW == color:
            self.__col_pos = {"x": 0, "y":0 }
