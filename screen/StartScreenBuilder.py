from .StartScreen import StartScreen
from .Struct import TextStruct, ButtonStruct
from .ScreenBuilder import ScreenBuilder

class StartScreenBuilder(ScreenBuilder):
    def __init__(self):
        super().__init__()
        pass

    # Builder method Override
    def SettingTitle(self):
        title = TextStruct()
        title.name = "Py Py Snake Game"
        title.col = 11 # 緑
        self.title = title
        pass

    def SettingButton(self):
        button = ButtonStruct()
        button.name = "Start!"
        button.name_col = 7 # 白
        button.back_cols = (2, 9) #赤茶、オレンジ
        self.buttons = [ button ]
        pass

    def GetBuildInstance(self):
        return StartScreen( self.title, self.buttons )
