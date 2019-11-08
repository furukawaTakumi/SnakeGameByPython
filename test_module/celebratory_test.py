import sys

sys.path.append('../')

from screen.Celebratory import Celebratory

def test_SelectCelebrateMsg():
    celebrate_msg = ["You are First!!", "You are Second!!", "You are Third!!"]
    for rank in range(1,4):
        assert celebrate_msg[rank-1] == Celebratory.SelectCelebrateMsg(rank), "ランクとお祝いのメッセージが一致しません"

    assert "You no Record. Try agein!" == Celebratory.SelectCelebrateMsg(4), "励ましのメッセージが送られていません"
    assert "You no Record. Try agein!" == Celebratory.SelectCelebrateMsg(14), "励ましのメッセージが送られていません"
    assert "You no Record. Try agein!" == Celebratory.SelectCelebrateMsg(0), "励ましのメッセージが送られていません"
    print("Celebratory.SelectCelebrateMsg() test pass!")


def DoneAllTest():
    test_SelectCelebrateMsg()
