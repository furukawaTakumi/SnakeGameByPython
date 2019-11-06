
class ScoreBoard:
    def __init__(self):
        # スタート画面に表示するスコアリスト生成
        self.filepath = "asset/score.txt"
        self.__score_list = []
        self.LoadScore()

    def LoadScore(self):
        templist = list()
        with open(self.filepath, mode='r') as file:
            for s in file.readlines():
                templist.append(int(s))

        self.__score_list = templist

    @property
    def score_list(self):
        return self.__score_list
