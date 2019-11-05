
class GameOverJudgement(object):
    """ゲームの終了判定をするクラス"""

    @staticmethod
    def JudgeSnakeOutsideField(snake_head_pos, field_size):
        if 8 <= snake_head_pos["x"] and snake_head_pos["x"] <= (field_size[1]-2)*8:
            if 8 <= snake_head_pos["y"] and snake_head_pos["y"] <= (field_size[0]-2)*8:
                return False
        return True

    @staticmethod
    def JudgeCollideHeadAndBody(snake_pos):
        for index in range(1, len(snake_pos)):
            if snake_pos[0]["x"] == snake_pos[index]["x"]:
                if snake_pos[0]["y"] == snake_pos[index]["y"]:
                    return True
        return False
