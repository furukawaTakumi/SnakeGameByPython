import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pass

App()
