
import pyxel

class SnakeBody():
    def __init__(self):
        self.yellow = {"x": 0, "y":0}
        self.blue = {"x": 8, "y":0}
        self.position = {"x":0, "y":0}
        pass


    def update(self):
        pass

    def draw(self):
        pyxel.blt(0, 0, 0, self.blue["x"], self.blue["y"], 8, 8)

        pass
