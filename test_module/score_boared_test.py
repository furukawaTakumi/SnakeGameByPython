import sys

sys.path.append('../')

from screen.ScoreBoard import ScoreBoard
from game_contents.Score import Score

boared = ScoreBoard()

def init():
    with open("asset/scoretest.txt", "w") as file:
        for i in range(99, 0, -3):
            file.write(str(i) + "\n")

def SettingScore(score_val):
    init()

    score = Score()
    for i in range(score_val):
        score.CountUp()
    score.SaveScore("asset/scoretest.txt")

def test_RankedRecord():
    SettingScore(50)
    ranking = boared.RankedRecord("asset/scoretest.txt")
    assert ranking == 18, "ランクが間違っています"

    SettingScore(78)
    ranking = boared.RankedRecord("asset/scoretest.txt")
    assert ranking == 9, "ランクが間違っています"

    SettingScore(100)
    ranking = boared.RankedRecord("asset/scoretest.txt")
    assert ranking == 1, "ランクが間違っています"

    print("ScoreBoard.RankedRecord() test pass!")


def test_top3():
    init()

    top3list = boared.Top3("asset/scoretest.txt")

    count = 99
    for i in top3list:
        assert i == count, "トップスリーの値ではないです。"
        count -= 3

    print("ScoreBoard.Top3() test pass!")


def DoneAllTest():
    test_top3()
    test_RankedRecord()
    pass
