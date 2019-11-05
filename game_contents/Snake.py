
import pyxel
from copy import deepcopy
from .SnakeBody import SnakeBody
from .SnakeHead import SnakeHead
from .BodyColor import BodyColor as bColor

class Snake():
    def __init__(self, pos, vec):
        self.__head = SnakeHead( pos, vec )
        self.__body = SnakeBody()
        self.__before_endpos = {"x": 0, "y":0 }
        pass

    def GetHeadPos(self):
        return self.__head.position

    def RespondToDirect(self):
        self.__head.RespondToDirect()

    def UpdatePosition(self):
        if not len(self.__body.body_parts):
            self.__before_endpos = deepcopy( self.__head.position )
        else:
            self.__before_endpos = deepcopy( self.__body.getEndPos() )
        self.__body.UpdatePosition( self.__head.position )
        self.__head.UpdatePosition()

    def DrawBody(self):
        self.__body.Draw()
        self.__head.Draw()
        pass

    def Growth(self):
        self.__body.Growth(self.__before_endpos)

    def CollectSnakeParts(self):
        res = list()
        res.append(self.__head.position)
        for a_body in self.__body.body_parts:
            res.append(a_body.position)
        return res
