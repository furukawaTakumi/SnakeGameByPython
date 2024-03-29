import sys

sys.path.append('../')

from screen.Ranking import Ranking
from game_contents.Score import Score

def init():
    with open("assets/scoretest.txt", "w") as file:
        lis = list()
        for i in range(99, 0, -3):
            lis.append( str(i) )
        file.writelines("\n".join(lis))

def SettingScore(score_val):
    init()

    score = Score()
    for i in range(score_val):
        score.CountUp()
    score.SaveScore("assets/scoretest.txt")

def test_ReadRecord():
    init()
    assert int(Ranking.ReadRecord("assets/scoretest.txt")) == 3, "スコアを正しく取得することができていません"
    print("Ranking.ReadRecord() test pass!")


def test_RankedRecord():
    SettingScore(50)
    rank = Ranking.RankedRecord("assets/scoretest.txt")
    assert rank == 18, "ランクが間違っています"

    SettingScore(78)
    rank = Ranking.RankedRecord("assets/scoretest.txt")
    assert rank == 9, "ランクが間違っています"

    SettingScore(100)
    rank = Ranking.RankedRecord("assets/scoretest.txt")
    assert rank == 1, "ランクが間違っています"

    print("Ranking.RankedRecord() test pass!")

def test_SortScoreAndReWrite():
    SettingScore(100)
    Ranking.SortScoreAndReWrite("assets/scoretest.txt")
    with open("assets/scoretest.txt", "r") as file:
        top = int( file.readline() )
    assert top == 100, "ソートが完了されていません"

    print("Ranking.SortScoreAndReWrite() test pass!")


def test_top3():
    init()

    top3list = Ranking.Top3("assets/scoretest.txt")

    count = 99
    for i in top3list:
        assert i == count, "トップスリーの値ではないです。"
        count -= 3

    print("Ranking.Top3() test pass!")


def DoneAllTest():
    test_top3()
    test_RankedRecord()
    test_SortScoreAndReWrite()
    test_ReadRecord()
    pass
