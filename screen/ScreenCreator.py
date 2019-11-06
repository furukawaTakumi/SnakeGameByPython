from .StartScreen import StartScreen
from .GameOverScreen import GameOverScreen
from .Struct import TextStruct, ButtonStruct


def CreateStartScreen():
    title = TextStruct()
    title.name = "Py Py Snake Game"
    title.col = 11 # 緑

    button = ButtonStruct()
    button.name = "Start!"
    button.name_col = 7 # 白
    button.back_cols = (2, 9) #赤茶、オレンジ

    return StartScreen(title, button)

def CreateGameOverScreen():
    title = TextStruct()
    title.name = "Game Over..."
    title.col = 8

    button = ButtonStruct()
    button.name = "Restart?"
    button.name_col = 7
    button.back_cols = (2, 9)

    return GameOverScreen(title,button)
