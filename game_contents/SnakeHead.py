
import pyxel
from copy import deepcopy

class SnakeHead():
    def __init__(self, pos, vec):
        self.__pos = pos
        self.__vector = deepcopy(vec)
        self.__selected_vec = deepcopy(vec)
        self.__picture_num = 3;
        pass

    @property
    def position(self):
        return self.__pos

    def Draw(self):
        pyxel.blt(self.__pos["x"], self.__pos["y"], 0, self.__picture_num*8, 0, 8, 8, 15)
        pass

    def UpdatePosition(self):
        self.__vector = self.__selected_vec
        self.__pos["x"] += self.__vector["x"] * 8
        self.__pos["y"] += self.__vector["y"] * 8

    """
    ユーザからの指示を受け付けるメソッド
    """
    def RespondToDirect(self):
        x = self.__vector["x"]
        y = self.__vector["y"]
        if pyxel.btn(pyxel.KEY_RIGHT):
            if x == 1 and y == 0:
                self.__selected_vec = {"x":0 , "y":1 }
                self.__picture_num = 4;
            if x == 0 and y == 1:
                self.__selected_vec = {"x":-1 , "y":0 }
                self.__picture_num = 5;
            if x == -1 and y == 0:
                self.__selected_vec = {"x":0 , "y":-1 }
                self.__picture_num = 2;
            if x == 0 and y == -1:
                self.__selected_vec = {"x":1 , "y":0 }
                self.__picture_num = 3;

        elif pyxel.btn(pyxel.KEY_LEFT):
            if x == 1 and y == 0:
                self.__selected_vec = {"x":0 , "y":-1 }
                self.__picture_num = 2;
            if x == 0 and y == 1:
                self.__selected_vec = {"x":1 , "y":0 }
                self.__picture_num = 3;
            if x == -1 and y == 0:
                self.__selected_vec = {"x":0 , "y":1 }
                self.__picture_num = 4;
            if x == 0 and y == -1:
                self.__selected_vec = {"x":-1 , "y":0 }
                self.__picture_num = 5;
        pass
