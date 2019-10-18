
import pyxel

class SnakeBody():
    """ col: 体の色を文字列で指定する str() """
    def __init__(self, pos, color):
        self.__pos = pos
        self.__chiled = None
        if color == "blue":
            self.__color = {"x": 8, "y":0}
        else: # 想定では yellow
            self.__color = {"x": 0, "y":0}
        pass

    @property
    def child(self):
        return self.__chiled

    def Draw(self):
        pyxel.blt(self.__pos["x"], self.__pos["y"], 0, self.__color["x"], self.__color["y"], 8, 8)
        if self.__chiled is not None:
            self.__chiled.Draw()
        pass

    def UpdatePosition(self, next_pos):
        temp_pos = self.__pos
        self.__pos["x"] = next_pos["x"]
        self.__pos["y"] = next_pos["y"]
        if self.__chiled is not None:
            self.__chiled.UpdatePosition(temp_pos)

    def SetChiled(self, col):
        if self.__chiled is not None:
            if self.__color == "blue":
                self.__chiled.SetChiled("yellow")
            else:
                self.__chiled.SetChiled("blue")
        else:
            self.__chiled = SnakeBody(self.__pos, col )
        pass
