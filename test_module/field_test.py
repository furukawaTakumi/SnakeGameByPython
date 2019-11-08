import sys

sys.path.append('../')

from pprint import pprint
import re
import copy
from game_contents.Field import Field
from game_contents.ParcelState import ParcelState as pState
from game_contents.SpecReader import SpecReader

reader = SpecReader("assets/spec.txt")
row = reader.spec["fieldrow"]
column = reader.spec["fieldcolmun"]
field = Field( (row,column) )

def sizeCheck():
    assert row == len(field.block_list), "行の数が{}ではありません".format(str(row))
    for r in range(0,row):
        assert column == len(field.block_list[r]), "{}行目の列の数が{}ではありません".format(str(r), str(column))

def test_field_set_field():
    # サイズのチェック
    sizeCheck()

    # 内部の値が正しいかをチェックしていく
    # まずテストするデータの作成
    raw_data = str()
    for r in range(0,row):
        for c in range(0,column):
            raw_data = raw_data + str(int(field.block_list[r][c]))

    # つぎに正解データの作成
    test_data_first_row = "%d{%d}" % (int(pState.ABYSS),column)
    test_data_middle_row = "(%d%d{%d}%d){%d}" % (int(pState.ABYSS), int(pState.NONE),column-2, int(pState.ABYSS), row-2)
    test_data_end_row = "%d{%d}" % (int(pState.ABYSS),column)
    test_data = test_data_first_row + test_data_middle_row + test_data_end_row

    assert re.fullmatch(test_data, raw_data) is not None, "block_listの要素が想定どうりの内容でありません"

    print("Field.set_field() test pass!")


def test_ResetField():
    snake_pos = [[3,5], [4,5], [row-1,column-1],[1,1]]
    field.ResetField(snake_pos)
    sizeCheck()
    for check_pos in snake_pos:
        assert field.block_list[check_pos[0]][check_pos[1]] == pState.SNAKE, "ResetField()でblock_listに値が正常に設定できていません"

    print("Field.ResetParcelState() test pass!")

def DoneAllTest():
    test_field_set_field()
    test_ResetField()
