
import pyxel
from .ParcelState import ParcelState

class Field:
    def __init__(self, size):
        self.size = size

        # Field ParcelState Set
        self.block_list = list(list())
        self.__set_field()

    def SetParcelState(self, pos, state_num):
        self.block_list[pos[0],pos[1]] = state_num

    def Draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.size[0]*8, self.size[1]*8)

    def ResetField(self, snake_pos):
        self.__set_field()
        for pos in snake_pos:
            self.SetParcelState(pos, ParcelState.SNAKE)
        pass

    def __set_field(self):
        for i in range(0,self.size[1]):
            line_temp = list()
            for j in range(0,self.size[0]):
                if i == 0:
                    line_temp.append(ParcelState.ABYSS)
                elif i == self.size[1]-1:
                    line_temp.append(ParcelState.ABYSS)
                elif j == 0:
                    line_temp.append(ParcelState.ABYSS)
                elif j == self.size[0]-1:
                    line_temp.append(ParcelState.ABYSS)
                else:
                    line_temp.append(ParcelState.NONE)
            self.block_list.append(line_temp)
