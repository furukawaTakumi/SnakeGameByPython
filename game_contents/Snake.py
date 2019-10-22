
import pyxel
from .SnakeBody import SnakeBody
from .SnakeHead import SnakeHead
from .BodyColor import BodyColor as bColor

class Snake():
    def __init__(self, pos):
        self.head = SnakeHead( pos )
        self.body = []
        self.growth_flag = False
        pass

    def RespondToDirect(self):
        self.head.RespondToDirect()

    def UpdatePosition(self):
        if pyxel.frame_count % 16 == 0:
            n = len( self.body )
            if 0 < len(self.body):
                for i in range(n-1, 1, -1):
                    self.body[i].position = self.body[i-1].position
                self.body[0] = self.head.position
            self.head.UpdatePosition()
            if self.growth_flag:
                self.__growth()
                self.growth_flag = False

    def DrawBody(self):
        self.head.Draw()
        for a_body in self.body:
            a_body.Draw()
        pass

    def GetPosition(self):
        res = list()
        res.append(self.head.position)
        for a_body in self.body:
            res.append(a_body.position)
        return res

    def __growth(self, pos):
        new_body_color = bColor.NONE
        if bColor.YELLOW == self.body[len(self.body)-1].color:
            new_body_color = bColor.BLUE
        else:
            new_body_color = bColor.YELLOW
        new_body = SnakeBody( pos, new_body_color )
        self.body.append(new_body)
        pass
