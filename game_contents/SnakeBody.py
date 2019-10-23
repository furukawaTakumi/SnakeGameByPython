
import pyxel
from .BodyParts import BodyParts
from .BodyColor import BodyColor as bColor

class SnakeBody():
    def __init__(self):
        self.__body = []
        self.__growthed_flag = False
        pass

    @property
    def isGrowthed(self):
        return self.__growthed_flag

    def Draw(self):
        for a_body in self.__body:
            a_body.Draw()


    def UpdatePosition(self, new_pos):
        if 0 >= len(self.__body):
            return

        n = len(self.__body) - 1
        for i in range(n-1, 1, -1): # 後ろから更新する
            self.__body[i].position = self.__body[i-1].position
        self.__body[0] = new_pos

    def Growth(self):
        parts = None
        if 0 == len( self.__body ) % 2:
            parts = BodyParts( bColor.YELLOW )
        else:
            parts = BodyParts( bColor.BLUE )

        self.__growthed_flag = True
