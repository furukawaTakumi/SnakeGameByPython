
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
        self.new_record_str = ["","",""]
        pass

    def CheckDiff(self):
        self.scoreboard.LoadScore()
        for index in range(0, len(self.scoreboard.score_list)):
            if self.before_score_list[index] != self.scoreboard.score_list[index]:
                self.new_record_str[index] = "← you recored!!"
        pass

    def ScreenUpdate(self):
        super().ScreenUpdate()
        self.CheckDiff()
        first = TextStruct( "1st : " +  str(self.scoreboard.score_list[0]) + self.new_record_str[0], 7 )
        second = TextStruct( "2nd : " + str(self.scoreboard.score_list[1]) + self.new_record_str[1], 7 )
        third = TextStruct( "3rd : " + str(self.scoreboard.score_list[2]) + self.new_record_str[2], 7 )
        self.new_record_str = ["","",""]
        pos = self.title_pos
        new_pos = list()
        new_pos.append( pyxel.width//2 - first.size[0] // 2 )
        new_pos.append( pos[1] + 15 )
        pyxel.text( new_pos[0], new_pos[1], first.name, first.col )
        new_pos[1] += 9
        pyxel.text( new_pos[0], new_pos[1], second.name, second.col )
        new_pos[1] += 9
        pyxel.text( new_pos[0], new_pos[1], third.name, third.col )
