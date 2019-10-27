import sys

sys.path.append('../')

from pprint import pprint
import re
from game_contents.Field import Field
from game_contents.ParcelState import ParcelState as pState

row = 11  # いずれファイルからコースのデータなどを読み込むようにしたい
column = 16
field = Field( (row,column) )

def test_field_set_field():
    # サイズのチェック
    assert row == len(field.block_list), "行の数が{}ではありません".format(str(row))
    for r in range(0,row):
        assert column == len(field.block_list[r]), "{}行目の列の数が{}ではありません".format(str(r), str(column))

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

test_field_set_field()
