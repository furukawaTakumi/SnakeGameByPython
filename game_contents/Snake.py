
import pyxel
from .SnakeBody import SnakeBody
from .SnakeHead import SnakeHead
from .BodyColor import BodyColor as bColor

class Snake():
    def __init__(self, pos):
        self.__head = SnakeHead( pos )
        self.__body = SnakeBody()
        pass

    def RespondToDirect(self):
        self.__head.RespondToDirect()

    def UpdatePosition(self):
        if pyxel.frame_count % 16 == 0:
            self.__head.UpdatePosition()
            self.__body.UpdatePosition( self.__head.position )


    def DrawBody(self):
        self.__head.Draw()
        self.__body.Draw()
        pass

    def GetPosition(self):
        res = list()
        res.append(self.head.position)
        for a_body in self.body:
            res.append(a_body.position)
        return res
