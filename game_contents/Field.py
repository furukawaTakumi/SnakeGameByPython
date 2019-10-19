
import pyxel
from .Parcel import Parcel

class Field:
    def __init__(self, size):
        self.size = (128,88)
        pass

    def Draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, self.size[0]//8, self.size[1]//8)
