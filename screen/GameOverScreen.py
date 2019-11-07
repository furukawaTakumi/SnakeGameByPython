
import pyxel
from copy import deepcopy
from .Screen import Screen
from .Struct import TextStruct
from .ScoreBoard import ScoreBoard


class GameOverScreen(Screen):
    def __init__(self, title, button):
        super().__init__(title, button)
        self.scoreboard = ScoreBoard()
        self.before_score_list = deepcopy( self.scoreboard.score_list )
        self.celebrate_txt = ["You are First!!", "You are Second!!", "You are third!!", ""]
        pass

    def ScreenUpdate(self, score):
        super().ScreenUpdate()
        idx = self.calcDiffScoreIdx(score)
        celebrate_txt = TextStruct(self.celebrate_txt[idx], 10)
        myrecord = TextStruct( "record: " + str( score ), 7 )
        pyxel.text( pyxel.width//2 - myrecord.size[0] // 2, self.title_pos[1]+15, myrecord.name, myrecord.col )
        pyxel.text( pyxel.width//2 - celebrate_txt.size[0] // 2, self.title_pos[1]+25, celebrate_txt.name, celebrate_txt.col )
