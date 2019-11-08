import pyxel
from .ScreenButton import ScreenButton
from .Struct import TextStruct, ButtonStruct

class Screen:
    """
    title: TextStruct
    button: ButtonStruct
    """
    def __init__(self, title, buttons):
        self.title = title
        self.title_pos = (pyxel.width//2 - title.size[0]//2, pyxel.height//4)
        self.btn_clicked = False

        self.button_dic = {}
        onestep = pyxel.width//(len(buttons)+1)
        for btn in buttons:
            btn_pos = (onestep-btn.size[0]//2, pyxel.height//4*3)
            self.button_dic[btn.name] = ScreenButton( btn, btn_pos )
            onestep += onestep

    def ScreenUpdate(self):
        pyxel.text(self.title_pos[0], self.title_pos[1], self.title.name, self.title.col)
        for btn in self.button_dic.values():
            btn.Draw()
        pass

    def PrepareDisplay(self):
        pass

    def isBtnClicked(self, btn_name):
        return self.button_dic[btn_name].isClicked()
