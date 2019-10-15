class Score:
    def __init__(self):
        self.__now_score = 0

        # スタート画面に表示するスコアリスト生成
        self.filepath = "asset/score.txt"
        self.__score_list = []

        with open(self.filepath, mode='r') as file:
            for s in file.readlines():
                self.__score_list.append(int(s))
        pass

    @property
    def score_list(self):
        return self.__score_list

    @property
    def now_score(self):
        return self.__now_score

    @now_score.setter
    def now_score(self, score):
        self.__now_score += score

    @score_list.setter
    def score_list(self, score):
        if self.__score_list[2] < score:
            self.__score_list.pop()
            self.__score_list.append(score)
            self.__score_list.sort(reverse=True)
            with open(self.filepath, mode='w') as file:
                write_list = [str(i) for i in self.__score_list]
                file.write( "\n".join(write_list) )
        pass
