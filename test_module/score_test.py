import sys

sys.path.append('../')

from game_contents.Score import Score
from game_contents.SpecReader import SpecReader

score = Score()

def test_init():
    assert score.score == 0, "スコアの初期化がうまくいっていません"

    reader = SpecReader("asset/spec.txt")
    pos = (reader.spec["score_pos_x"], reader.spec["score_pos_y"])
    assert pos[0] == score.pos[0], "スコアの初期位置xが間違っています"
    assert pos[1] == score.pos[1], "スコアの初期位置yが間違っています"
    print("Score.__init__() test pass!")


def test_CountUp():
    for a in range(1,100):
        score.CountUp()
        assert score.score == a, "スコアのカウントがおかしいです。期待する値:{0}, 実際の値:{1}".format(a, score.score)
    print("Score.CountUp() test pass!")

def test_WriteScore():
    score = Score()
    with open("asset/scoretest.txt", "w") as file:
        file.write("")

    for i in range(1,100):
        score.WriteScore("asset/scoretest.txt")
        score.CountUp()

    with open("asset/scoretest.txt", "r") as file:
        count = 0
        for line in file.readlines():
            assert count == int(line), "書き込みがうまく行われていません"
            count += 1
    print("Score.WriteScore() test pass!")



def DoneAllTest():
    test_init()
    test_CountUp()
    test_WriteScore()
