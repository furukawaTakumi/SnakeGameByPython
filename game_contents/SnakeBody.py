
import pyxel
from .BodyColor import BodyColor as bColor

class SnakeBody():
    """ col: 体の色を文字列で指定する str() """
    def __init__(self, pos, color):
        self.position = pos

        if bColor.BLUE == color:
            self.__pic_pos = {"x": 8, "y": 0}
        elif bColor.YELLOW == color:
            self.__pic_pos = {"x": 0, "y": 0}
        pass

    def Draw(self):
        pyxel.blt(self.__pos["x"], self.__pos["y"], 0, self.__pic_pos["x"], self.__pic_pos["y"], 8, 8)
