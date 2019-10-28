
from .SpecReader import SpecReader
from .Snake import Snake
from .Field import Field

class GameController():
    def __init__(self):
        self.__contents_spec = SpecReader("spec.txt")
        snake_pos = { "x": self.__contents_spec["init_snake_pos_x"], "y":self.__contents_spec["init_snake_pos_y"]}
        self.__snake = Snake(snake_pos)
        self.__field = Field()
