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

    return StartScreen(title, [button])

def CreateGameOverScreen():
    title = TextStruct()
    title.name = "Game Over..."
    title.col = 8

    restart_btn = ButtonStruct()
    restart_btn.name = "Restart?"
    restart_btn.name_col = 7
    restart_btn.back_cols = (2, 9)

    totitle_btn = ButtonStruct()
    totitle_btn.name = "toTitle"
    totitle_btn.name_col = 7
    totitle_btn.back_cols = (2, 9)

    return GameOverScreen(title, [restart_btn, totitle_btn])
