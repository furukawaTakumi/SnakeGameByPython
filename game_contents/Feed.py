
import pyxel
import random

class Feed:
    def __init__(self, field_size):
        self.__is_exist = False
        self.__feed_pos = [-1,-1]

    @property
    def is_exist(self):
        return self.__is_exist

    @property
    def feed_pos(self):
        return self.__feed_pos

    def Drow(self):
        if self.__is_exist:
            pyxel.blt(self.feed_pos[0], self.feed_pos[1], 0, 6*8, 0, 8, 8)

    # field_sizeは生成範囲指定を行うもの。リストまたはタプルで渡す。
    def CreateFeed(self, snake_pos, field_size):
        # 適切な位置が帰ってくるまでサイコロを振り続ける
        while True:
            self.__feed_pos[0] = random.sample( range(1, field_size[0]-1), 1 )[0] # 長さ1のリストを生成する
            self.__feed_pos[1] = random.sample( range(1, field_size[1]-1), 1 )[0]

            break_flag = True
            for pos in snake_pos:
                if pos["x"] == self.__feed_pos[0] and pos["y"] == self.__feed_pos[1]:
                    break_flag = False
            if break_flag:
                break

        self.__is_exist = True

    def DeleteFeed(self):
        if self.__is_exist:
            self.__feed_pos[0] = -1
            self.__feed_pos[1] = -1
            self.__is_exist = False
