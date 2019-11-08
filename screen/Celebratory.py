
from .Struct import TextStruct

class Celebratory():
    @staticmethod
    def SelectCelebrateMsg(rank):
        celebrate_txt = ["You are First!!", "You are Second!!", "You are Third!!"]
        if 1 <= rank and rank <= 3:
            return TextStruct( celebrate_txt[rank-1], 10 )
        return TextStruct( "You no Record. Try agein!", 7)
