
class ScoreBoard:
    def __init__(self):
        # スタート画面に表示するスコアリスト生成
        self.__score_list = []

    def Top3(self, filepath="asset/score.txt"):
        self.__score_list = []
        with open(filepath, mode='r') as file:
            for i in range(3):
                self.__score_list.append( int( file.readline() ) )
        return self.__score_list

    def RankedRecord(self, filepath="asset/score.txt"):
        with open(filepath, "r") as file:
            scores = file.readlines()

        recored = int(scores[-1]) # ファイルの最終行に新しい記録を追加しているからそれをまず取得
        scores.pop(-1)
        rank = len(scores)+1

        for score in scores[::-1]:
            if recored > int(score):
                rank -= 1
        return rank

    def SortScoreAndReWrite(self, filepath="asset/score.txt"):
        with open(filepath, "r") as file:
            scores = file.readlines()

        int_scores = [int(i) for i in scores]
        int_scores.sort(reverse=True)
        scores = [str(s) for s in int_scores]

        with open(filepath, "w") as file:
            file.writelines( "\n".join(scores) )


    @property
    def score_list(self):
        return self.__score_list
