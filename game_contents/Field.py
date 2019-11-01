
import pyxel
from random import sample
from .ParcelState import ParcelState

class Field:
    def __init__(self, size):
        self.size = size # (行,列)
        self.feed_pos = [-1,-1]

        # Field ParcelState Set
        self.block_list = list(list())
        for i in range(0, self.size[0]):
            temp_list = list()
            for j in range(0, self.size[1]):
                temp_list.append(ParcelState.UNDEFINE)
            self.block_list.append(temp_list)
        self.__set_field()

    def Draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.size[0]*8, self.size[1]*8)
        if self.__range_check(feed_pos, 1):
            pyxel.blt(self.feed_pos[0], self.feed_pos[1], 0, 6*8, 0, 8, 8)

    def CreateFeed(self):
        # 適切な位置が帰ってくるまでサイコロを振り続ける
        while True:
            self.feed_pos[0] = sample( range(1, self.size[0]-1), 1 )[0] # 長さ1のリストを生成する
            self.feed_pos[1] = sample( range(1, self.size[1]-1), 1 )[0]

            if ParcelState.NONE == self.block_list[self.feed_pos[0]][self.feed_pos[1]]:
                break

        self.block_list[self.feed_pos[0]][self.feed_pos[1]] = ParcelState.FEED

    def DeleteFeed(self):
        if self.__range_check(self.feed_pos, 1):
            self.block_list[self.feed_pos[0]][self.feed_pos[1]] = ParcelState.NONE
            self.feed_pos[0] = -1
            self.feed_pos[1] = -1

    def ResetField(self, snake_pos):
        self.__set_field()
        for pos in snake_pos:
            self.block_list[pos[0]][pos[1]] = ParcelState.SNAKE
        if self.__range_check(self.feed_pos, 1):
            self.block_list[self.feed_pos[0]][self.feed_pos[1]] = ParcelState.FEED
        pass

    def __range_check(self, check_pos, option=0):
        if 0+option > check_pos[0] or 0+option > check_pos[1]:
            return False
        if self.size[0]-option <= check_pos[0] or self.size[1]-option <= check_pos[1]:
            return False
        return True

    def __set_field(self):
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                if i == 0:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif i == self.size[0]-1:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif j == 0:
                    self.block_list[i][j] = ParcelState.ABYSS
                elif j == self.size[1]-1:
                    self.block_list[i][j] = ParcelState.ABYSS
                else:
                    self.block_list[i][j] = ParcelState.NONE
