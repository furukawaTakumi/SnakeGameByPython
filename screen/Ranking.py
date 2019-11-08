
class Ranking:
    @staticmethod
    def Top3(filepath="assets/score.txt"): #staticmethodにしたらデフォルト引数が固定化されてしまった
        score_list = []
        with open(filepath, mode='r') as file:
            for i in range(3):
                score_list.append( int( file.readline() ) )
        return score_list

    @staticmethod
    def ReadRecord(filepath="assets/score.txt"):
        with open(filepath, "r") as file:
            scores = file.readlines()
        return int(scores[len(scores)-1])

    @staticmethod
    def RankedRecord(filepath="assets/score.txt"):
        with open(filepath, "r") as file:
            scores = file.readlines()

        recored = int(scores[-1]) # ファイルの最終行に新しい記録を追加しているからそれをまず取得
        rank = len(scores)

        for score in scores[::-1]:
            if recored > int(score):
                rank -= 1
        return rank

    @staticmethod
    def SortScoreAndReWrite(filepath="assets/score.txt"):
        with open(filepath, "r") as file:
            scores = file.readlines()

        int_scores = [int(i) for i in scores]
        int_scores.sort(reverse=True)

        scores = [str(s) for s in int_scores]

        with open(filepath, "w") as file:
            file.writelines( "\n".join(scores) )
