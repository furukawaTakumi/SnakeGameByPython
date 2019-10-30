
from .SpecReader import SpecReader
from .Snake import Snake
from .Field import Field
from .ParcelState import ParcelState as pState

class GameController():
    def __init__(self):
        reader = SpecReader("spec.txt")
        snake_pos = {
            "x": reader.spec["init_snake_pos_x"],
            "y": reader.spec["init_snake_pos_y"]
        }
        snake_vec = {
            "x": reader.spec["init_snake_vec_x"],
            "y": reader.spec["init_snake_vec_y"]
        }
        self.__snake = Snake(snake_pos, snake_vec)

        self.__field_size = ( reader.spec["fieldrow"], reader.spec["fieldcolmun"] )
        self.__field = Field(self.__field_size)
