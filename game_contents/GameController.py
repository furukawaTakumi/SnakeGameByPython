
import pyxel
from .SpecReader import SpecReader
from .Snake import Snake
from .Field import Field
from .ParcelState import ParcelState as pState

class GameController():
    def __init__(self):
        reader = SpecReader("asset/spec.txt")
        snake_pos = {
            "x": reader.spec["init_snake_pos_x"],
            "y": reader.spec["init_snake_pos_y"]
        }
        snake_vec = {
            "x": reader.spec["init_snake_vec_x"],
            "y": reader.spec["init_snake_vec_y"]
        }
        self.__snake = Snake(snake_pos, snake_vec)

        field_size = ( reader.spec["fieldrow"], reader.spec["fieldcolmun"] )
        self.__field = Field(field_size)

    def UpdateData(self):
        self.__snake.RespondToDirect()
        if pyxel.frame_count % 16 == 0:
            self.__snake.UpdatePosition()

    def UpdateDisplay(self):
        self.__field.Draw()
        self.__snake.DrawBody()
