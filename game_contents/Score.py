
from pyxel import text
from .SpecReader import SpecReader

class Score():
    """ゲーム中のスコアを計算、表示する"""

    def __init__(self):
        self.__score = 0
        self.__disp_str = "SCORE: {}"
        # self.__rank

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

    def rank(self):
        rank = -1
        for s in range(0,len(score_list)):
            if self.__score > score_list[s]:
                self.__rank = s
                break
        return rank

    def SaveScore(self, filepath="asset/score.txt"): #テストしやすいように通常利用するパスをデフォルト引数とした
        with open(filepath, mode='a') as file:
            file.write( "\n" + str( self.__score ) )
