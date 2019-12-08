
from .GameOverScreen import GameOverScreen
from .Struct import TextStruct, ButtonStruct
from .ScreenBuilder import ScreenBuilder
"""
BuilderパターンのうちのConcreteBuilder役を務めるクラス
"""
class GameOverScreenBuilder(ScreenBuilder):
    def __init__(self):
        super().__init__()
        pass

    # Builder Method Override 
    def SettingTitle(self):
        title = TextStruct()
        title.name = "Game Over..."
        title.col = 8
        self.title = title
        pass

    # Builder Method Override 
    def SettingButton(self):
        restart_btn = ButtonStruct()
        restart_btn.name = "Restart?"
        restart_btn.name_col = 7
        restart_btn.back_cols = (2, 9)

        totitle_btn = ButtonStruct()
        totitle_btn.name = "toTitle"
        totitle_btn.name_col = 7
        totitle_btn.back_cols = (2, 9)
        self.buttons = [ restart_btn, totitle_btn ]

    # 作成したインスタンスを得るためのメソッド
    def GetBuildInstance(self):
        return GameOverScreen( self.title, self.buttons )