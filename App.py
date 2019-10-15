import pyxel
from screen.Screen import Screen
from screen.ScreenCreator import CreateStartScreen

class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.mouse(True)

        self.startScreen = CreateStartScreen()
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.startScreen.ScreenUpdate()
        pass

App()
