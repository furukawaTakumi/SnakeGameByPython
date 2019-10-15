import pyxel
from .ScreenButton import ScreenButton
from .Struct import TextStruct, ButtonStruct

class Screen:
    """
    title: TextStruct
    button: ButtonStruct
    """
    def __init__(self, title, button):
        self.title = title
        self.title_pos = (pyxel.width//2 - title.size[0]//2, pyxel.height//4)
        self.btn_pos = (pyxel.width//2 - button.size[0]//2, pyxel.height//4*3)
        self.startFlag = False
        self.start_btn = ScreenButton( button, self.btn_pos )

    def ScreenUpdate(self):
        pyxel.text(self.title_pos[0], self.title_pos[1], self.title.name, self.title.col)
        self.startFlag = self.start_btn.isClicked()
        pass

    def isStart(self):
        return self.startFlag
