
import pyxel
from .SnakeBody import SnakeBody
from .SnakeHead import SnakeHead

class Snake():
    def __init__(self, pos):
        self.head = SnakeHead( pos )
        self.body = []
        pass

    def Update(self):
        before_head_pos = self.head.position
        self.head.Update()

        n = len( self.body )
        for i in range(n-1):
            before_pos = self.body[n-i].position
            # 次回、ケツからポジションを更新していく処理を記述する




    def Draw(self):
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

    def Growth(self):
        pass
