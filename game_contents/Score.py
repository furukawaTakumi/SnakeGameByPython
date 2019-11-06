
from pyxel import text
from .SpecReader import SpecReader

class Score():
    """ゲーム中のスコアを計算、表示する"""

    def __init__(self):
        self.__score = 0
        self.__disp_str = "SCORE: {}"

        reader = SpecReader("asset/spec.txt")
        x = reader.spec["score_pos_x"]
        y = reader.spec["score_pos_y"]
        self.__pos = (x, y)

    @property
    def score(self):
        return self.__score

    @property
    def pos(self):
        return self.__pos

    def DrawScore(self):
        text(self.__pos[0], self.__pos[1], self.__disp_str.format(self.__score), 7 )
        pass

    def CountUp(self):
        self.__score += 1

    def CleanUp(self):
        self.__score = 0

    def WriteScore(self, filename):
        score_list = list()
        with open(filename, mode='r') as file:
            for line in file.readlines():
                score_list.append(int(line))

        score_list.append( self.__score )
        score_list.sort(reverse=True)
        with open(filename, mode='w') as file:
            for i in range(0,3):
                file.write( str( score_list[i] ) + "\n" )
