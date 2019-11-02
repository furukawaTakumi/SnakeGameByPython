import sys

sys.path.append('../')

from pprint import pprint
from game_contents.Feed import Feed
from game_contents.SpecReader import SpecReader

reader = SpecReader("asset/spec.txt")
row = reader.spec["fieldrow"]
column = reader.spec["fieldcolmun"]
field_size = (row, column)
feed = Feed(field_size)

def test_init():
    assert feed.is_exist == False, "Feedインスタンス生成時からFeedが存在しています"
    assert feed.feed_pos[0] == -1, "初期値が間違っています"
    assert feed.feed_pos[1] == -1, "初期値が間違っています"
    print("Feed.__init__() test pass!")


def test_CreateFeed():
    snake_pos = list()
    for j in range(1, column-1):
        for i in range(1, row//2):
            snake_pos.append( { "x":j, "y":i } )

    feed.CreateFeed(snake_pos, field_size)
    for j in range(1, column-1):
        for i in range(1, row//2):
            assert feed.feed_pos[0] != j or feed.feed_pos[1] != i, "餌を生成してはいけない位置に餌を生成しています(餌の位置{0},{1} )".format(feed.feed_pos[0], feed.feed_pos[1])
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
