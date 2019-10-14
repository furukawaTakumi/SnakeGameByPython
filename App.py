import pyxel
from screen.StartScreen import StartScreen

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)

        self.startScreen = StartScreen()
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.startScreen.ScreenUpdate()
        pass

App()
