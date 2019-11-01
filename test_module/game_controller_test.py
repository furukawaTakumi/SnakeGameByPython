import sys

sys.path.append('../')

from pprint import pprint
import os
from game_contents.GameController import GameController

def test_init():
    controller = GameController()

    print("GameController.__init__() test pass!")


def DoneAllTest():
    test_init()
