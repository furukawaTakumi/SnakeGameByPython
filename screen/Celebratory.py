
class Celebratory():
    @staticmethod
    def SelectCelebrateMsg(rank):
        celebrate_txt = ["You are First!!", "You are Second!!", "You are Third!!"]
        if 1 <= rank and rank <= 3:
            return celebrate_txt[rank-1]
        return "You no Record. Try agein!"
