
import pyxel
from .Snake import Snake
from .Field import Field

class GameLosic:
    def __init__(self):
        self.field = Field((16,11))
        self.snake = Snake({"x": 0, "y": 0})
