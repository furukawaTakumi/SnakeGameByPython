
import sys

sys.path.append('../')

from game_contents.GameOverJudgement import GameOverJudgement
from game_contents.SpecReader import SpecReader

spec = SpecReader("asset/spec.txt")
field_size = ( spec.spec["fieldrow"], spec.spec["fieldcolmun"] )
judgement = None

def test_JudgeSnakeOutsideField():
    for x in range(0,spec.spec["fieldcolmun"]):
        snake_head_pos = {"x":x, "y":0 }
        assert GameOverJudgement.JudgeSnakeOutsideField(snake_head_pos, field_size ), "蛇は場外にいます。蛇の位置：(x,y) = ({0},{1})".format(snake_head_pos["x"], snake_head_pos["y"])
        snake_head_pos = {"x":x, "y":spec.spec["fieldrow"]-1 }
        assert GameOverJudgement.JudgeSnakeOutsideField(snake_head_pos, field_size ), "蛇は場外にいます。蛇の位置：(x,y) = ({0},{1})".format(snake_head_pos["x"], snake_head_pos["y"])

    for y in range(0,spec.spec["fieldrow"]):
        snake_head_pos = {"x":0, "y":y }
        assert GameOverJudgement.JudgeSnakeOutsideField(snake_head_pos, field_size ), "蛇は場外にいます。蛇の位置：(x,y) = ({0},{1})".format(snake_head_pos["x"], snake_head_pos["y"])
        snake_head_pos = {"x":spec.spec["fieldcolmun"]-1, "y":y }
        assert GameOverJudgement.JudgeSnakeOutsideField(snake_head_pos, field_size ), "蛇は場外にいます。蛇の位置：(x,y) = ({0},{1})".format(snake_head_pos["x"], snake_head_pos["y"])

    for x in range(1, spec.spec["fieldcolmun"]-1):
        for y in range(1, spec.spec["fieldrow"]-1):
            snake_head_pos = {"x":x, "y":y }
            assert not GameOverJudgement.JudgeSnakeOutsideField(snake_head_pos, field_size), "蛇は場内にいます。蛇の位置：(x,y) = ({0},{1})".format(snake_head_pos["x"], snake_head_pos["y"])

    print("GameOverJudgement.JudgeSnakeOutsideField() test pass!")

def test_JudgeCollideHeadAndBody():
    sanke_pos = [{"x":0, "y":0},{"x":0, "y":0}]
    assert GameOverJudgement.JudgeCollideHeadAndBody(sanke_pos), "蛇の体と頭の位置が重なり合うのに、メソッドはFalseを返しています"

    sanke_pos = [{"x":0, "y":0},{"x":1, "y":0}]
    assert not GameOverJudgement.JudgeCollideHeadAndBody(sanke_pos), "蛇の体と頭の位置が重なりあっていないのに、メソッドはTrueを返しています"
    sanke_pos = [{"x":0, "y":0},{"x":0, "y":1}]
    assert not GameOverJudgement.JudgeCollideHeadAndBody(sanke_pos), "蛇の体と頭の位置が重なりあっていないのに、メソッドはTrueを返しています"

    snake_pos = [{"x":0,"y":0}]
    assert not GameOverJudgement.JudgeCollideHeadAndBody(sanke_pos), "蛇の体と頭の位置が重なりあっていないのに、メソッドはTrueを返しています"

def DoneAllTest():
    test_init()
    test_JudgeSnakeOutsideField()
    test_JudgeCollideHeadAndBody()
    pass
