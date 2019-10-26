import sys

sys.path.append('../')

from game_contents.Field import Field

row = 11  # いずれファイルからコースのデータなどを読み込むようにしたい
column = 16
field = Field( (row,column) )

def test_field_set_field():
    assert row == len(field.block_list), "行の数が{}ではありません".format(str(row))
    for r in range(0,row):
        assert column == len(field.block_list[r]), "{}行目の列の数が{}ではありません".format(str(r), str(column))

    print("Field.set_field() test pass!")

test_field_set_field()
