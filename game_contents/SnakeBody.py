
import pyxel
from copy import deepcopy
from .BodyParts import BodyParts
from .BodyColor import BodyColor as bColor

class SnakeBody():
    def __init__(self):
        self.__body = []
        self.__growthed_flag = False
        pass

    @property
    def body_parts(self):
        return self.__body

    def getEndPos(self):
        return self.__body[len(self.__body)-1].position

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
        for i in range(n, 0, -1):
            self.__body[i].position = self.__body[i-1].position
        self.__body[0].position = deepcopy(new_pos)

    def Growth(self, before_endpos):
        parts = None
        if not len( self.__body ):
            parts = BodyParts( deepcopy(before_endpos), bColor.YELLOW )
        elif len( self.__body ) % 2:
            parts = BodyParts( deepcopy(before_endpos), bColor.BLUE )
        else:
            parts = BodyParts( deepcopy(before_endpos), bColor.YELLOW )

        self.__body.append(parts)
        self.__growthed_flag = True
        pyxel.play(0, 16)
