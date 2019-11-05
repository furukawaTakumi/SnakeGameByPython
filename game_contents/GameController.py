
import pyxel
from .SpecReader import SpecReader
from .Snake import Snake
from .Field import Field
from .Feed import Feed
from .Score import Score
from .ParcelState import ParcelState as pState
from .GameOverJudgement import GameOverJudgement

class GameController():
    def __init__(self):
        reader = SpecReader("asset/spec.txt")
        snake_pos = {
            "x": reader.spec["init_snake_pos_x"],
            "y": reader.spec["init_snake_pos_y"]
        }
        snake_vec = {
            "x": reader.spec["init_snake_vec_x"],
            "y": reader.spec["init_snake_vec_y"]
        }
        self.__snake = Snake(snake_pos, snake_vec)

        field_size = ( reader.spec["fieldrow"], reader.spec["fieldcolmun"] )
        self.__field = Field(field_size)
        self.__feed = Feed()
        self.__score = Score()

    def UpdateData(self):
        self.__snake.RespondToDirect()
        if pyxel.frame_count % 16 == 0:
            self.__snake.UpdatePosition()
            self.__collideSnakeAndFeed()

        if not self.__feed.is_exist:
            self.__feed.CreateFeed(self.__snake.CollectSnakeParts(), self.__field.size )

    def UpdateDisplay(self):
        self.__field.Draw()
        self.__snake.DrawBody()
        self.__score.DrawScore()
        self.__feed.Draw()

    def __collideSnakeAndFeed(self):
        if self.__feed.feed_pos[0] == self.__snake.GetHeadPos()["y"]:
            if self.__feed.feed_pos[1] == self.__snake.GetHeadPos()["x"]:
                self.__snake.Growth()
                self.__score.CountUp()
                self.__feed.DeleteFeed()
                pyxel.play(0, 16)

    def CheckGameOver(self):
        if GameOverJudgement.JudgeSnakeOutsideField(self.__snake.GetHeadPos(), self.__field.size):
            pyxel.play(0, 17)
            return True

        if GameOverJudgement.JudgeCollideHeadAndBody(self.__snake.CollectSnakeParts()):
            pyxel.play(0, 17)
            return True
        return False
