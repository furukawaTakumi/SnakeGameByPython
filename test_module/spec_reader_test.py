import sys

sys.path.append('../')

from pprint import pprint
import os
from game_contents.SpecReader import SpecReader

def test_init():
    reader = SpecReader("assets/spec.txt")
    assert reader.spec["testdata_int"] == 0, "SpecReaderクラスにint型数値がうまく設定できませんでした"
    assert reader.spec["testdata_str"] == "0", "SpecReaderクラスに文字列がうまく設定できませんでした"
    print("SpecReader.__init__() test pass!")

def DoneAllTest():
    test_init()
