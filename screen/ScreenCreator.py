from .StartScreen import StartScreen
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
