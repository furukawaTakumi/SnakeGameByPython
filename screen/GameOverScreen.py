
import pyxel
from copy import deepcopy
from .Screen import Screen
from .Struct import TextStruct
from .Ranking import Ranking
from .Celebratory import Celebratory


class GameOverScreen(Screen):
    def __init__(self, title, button):
        super().__init__(title, button)
        self.record = 0
        pass

    def PrepareDisplay(self):
        self.score_rank = Ranking.RankedRecord()
        self.record = Ranking.ReadRecord()
        Ranking.SortScoreAndReWrite()

    def ScreenUpdate(self):
        super().ScreenUpdate()
        celebrate_txt = Celebratory.SelectCelebrateMsg(self.score_rank)
        myrecord = TextStruct( "record: " + str( self.record ), 7 )
        pyxel.text( pyxel.width//2 - myrecord.size[0] // 2, self.title_pos[1]+15, myrecord.name, myrecord.col )
        pyxel.text( pyxel.width//2 - celebrate_txt.size[0] // 2, self.title_pos[1]+25, celebrate_txt.name, celebrate_txt.col )
