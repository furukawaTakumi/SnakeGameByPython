import pyxel
from .ScreenButton import ScreenButton

class StartScreen:
    def __init__(self):
        self.title = "PyPy Snake Game"
        self.title_col = 11
        self.start_btn = ScreenButton((20,10), (1,2), (pyxel.width//2.5,pyxel.height//4*3), (" Start! ", 7) )
        self.startFlag = False

    def ScreenUpdate(self):
        pyxel.text(pyxel.width//2.5,pyxel.height//7, self.title, self.title_col)
        self.startFlag = self.start_btn.isClicked()
        pass

    def isStart(self):
        return self.startFlag
