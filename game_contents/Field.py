
import pyxel
from .Parcel import Parcel

class Field:
    def __init__(self, size):
        self.size = list()
        if size[0] % 8 != 0:
            self.size.append( size[0] - size[0]%8 )
        if size[1] % 8 != 0:
            self.size.append( size[1] - size[1]%8 )

        pass

    def Draw(self):
        origin_x = pyxel.width//2 - self.size[0]//2
        origin_y = pyxel.height//2 - self.size[1]//2
        pyxel.bltm(origin_x, origin_y, 0, 0, 0, 16, 11)
