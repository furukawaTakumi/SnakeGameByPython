
from random import sample

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

        field_size = ( reader.spec["fieldrow"], reader.spec["fieldcolmun"] )
        self.__field = Field(field_size)

    def CreateFeed(self):
        row_pos = len( self.__field.block_list )
        column_pos = len( self.__field.block_list[0] )

        # 適切な位置が帰ってくるまでサイコロを振り続ける
        create_pos_x = 0
        create_pos_y = 0
        while True:
            create_pos_x = sample( range(1, column_pos-1), 1 )[0] # 長さ1のリストを生成する
            create_pos_y = sample( range(1, row_pos-1), 1 )[0]

            if pState.NONE == self.__field.block_list[create_pos_x][create_pos_y]:
                break

        self.__field.block_list[create_pos_x][create_pos_y] = pState.FEED
