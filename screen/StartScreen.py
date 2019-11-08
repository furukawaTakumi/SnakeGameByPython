import pyxel
from .Screen import Screen
from .Struct import TextStruct, ButtonStruct
from .Ranking import Ranking

class StartScreen(Screen):
    def __init__(self, title, button):
        super().__init__(title, button)
        self.PrepareDisplay()
        pass

    def PrepareDisplay(self):
        self.__score_top3 = Ranking.Top3()


    def ScreenUpdate(self):
        super().ScreenUpdate()
        first = TextStruct( "1st : " +  str(self.__score_top3[0]), 7 )
        second = TextStruct( "2nd : " + str(self.__score_top3[1]), 7 )
        third = TextStruct( "3rd : " + str(self.__score_top3[2]), 7 )
        pos = self.title_pos
        new_pos = list()
        new_pos.append( pyxel.width//2 - first.size[0] // 2 )
        new_pos.append( pos[1] + 15 )
        pyxel.text( new_pos[0], new_pos[1], first.name, first.col )
        new_pos[1] += 9
        pyxel.text( new_pos[0], new_pos[1], second.name, second.col )
        new_pos[1] += 9
        pyxel.text( new_pos[0], new_pos[1], third.name, third.col )
        pass
