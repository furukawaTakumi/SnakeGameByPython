import sys

sys.path.append('../')

from pprint import pprint
from game_contents.Feed import Feed
from game_contents.SpecReader import SpecReader

reader = SpecReader("asset/spec.txt")
row = reader.spec["fieldrow"]
column = reader.spec["fieldcolmun"]
field_size = (row, column)
feed = Feed()

def test_init():
    assert feed.is_exist == False, "Feedインスタンス生成時からFeedが存在しています"
    assert feed.feed_pos[0] == -1, "初期値が間違っています"
    assert feed.feed_pos[1] == -1, "初期値が間違っています"
    print("Feed.__init__() test pass!")


def test_CreateFeed():
    snake_pos = list()
    for j in range(1, column-1):
        for i in range(1, row//2):
            snake_pos.append( { "x":j*8, "y":i*8 } )

    feed.CreateFeed(snake_pos, field_size)
    for j in range(1, column-1):
        for i in range(1, row//2):
            assert 1*8 <= feed.feed_pos[0] and feed.feed_pos[0] <= (row - 1)*8, "生成された餌の行範囲が規定の範囲内に収まっていません(生成された行：{})".format(feed.feed_pos[0])
            assert 1*8 <= feed.feed_pos[1] and feed.feed_pos[1] <= (column - 1)*8, "生成された餌の列範囲が規定の範囲内に収まっていません(生成された列：{})".format(feed.feed_pos[1])
            assert feed.feed_pos[1] != j*8 or feed.feed_pos[0] != i*8, "餌を生成してはいけない位置に餌を生成しています(餌の位置{0},{1} )".format(feed.feed_pos[0], feed.feed_pos[1])
    assert feed.is_exist, "餌生成フラグがTrueになっていません"
    # print("(餌の位置{0},{1} )".format(feed.feed_pos[0], feed.feed_pos[1]))


def test_DeleteFeed():
    feed.DeleteFeed()

    assert not feed.is_exist, "餌の存在を消せていません"
    assert feed.feed_pos[0] == -1, "餌の行位置が初期化されていません"
    assert feed.feed_pos[1] == -1, "餌の列位置が初期化されていません"

def DoneAllTest():
    test_init()
    for i in range(1000):
        test_CreateFeed()
        test_DeleteFeed()
    print("Feed.CreateFeed() test pass!")
    print("Feed.DeleteFeed() test pass!")
