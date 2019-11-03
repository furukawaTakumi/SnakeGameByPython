
import pyxel
from .ParcelState import ParcelState

class Field:
    def __init__(self, size):
        self.__size = size # (行,列)

        # Field ParcelState Set
        self.block_list = list(list())
        for i in range(0, self.__size[0]):
            temp_list = list()
            for j in range(0, self.__size[1]):
                temp_list.append(ParcelState.UNDEFINE)
            self.block_list.append(temp_list)
        self.__set_field()

    @property
    def size(self):
        return self.__size

    def Draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.__size[0]*8, self.__size[1]*8)

    def ResetField(self, snake_pos):
        self.__set_field()
        for pos in snake_pos:
            self.block_list[pos[0]][pos[1]] = ParcelState.SNAKE

    def __set_field(self):
        for i in range(0, self.__size[0]):
            for j in range(0, self.__size[1]):
                if i == 0:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif i == self.__size[0]-1:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif j == 0:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif j == self.__size[1]-1:
                    self.block_list[i][j] = ParcelState.ABYSS
                else:
                    self.block_list[i][j] = ParcelState.NONE
