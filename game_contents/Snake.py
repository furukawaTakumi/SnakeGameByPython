
import pyxel
from .SnakeBody import SnakeBody
from .SnakeHead import SnakeHead

class Snake():
    def __init__(self, pos):
        self.head = SnakeHead( pos )
        self.body = None
        pass

    def Update(self):
        self.head.Update()

    def Draw(self):
        self.head.Draw()

        pass

    def Growth(self):
        pass
