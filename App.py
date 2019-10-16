import pyxel
from screen.ScreenCreator import CreateStartScreen
from GameStatus import GameStatus

class App:
    def __init__(self):
        pyxel.init(130, 90)
        pyxel.mouse(True)
        self.now_status = GameStatus.START
        self.startScreen = CreateStartScreen()
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        if self.now_status == GameStatus.START:
            self.startScreen.ScreenUpdate()
            if self.startScreen.isBtnClicked():
                self.now_status = GameStatus.GAME

        elif self.now_status == GameStatus.GAME:
            pass
        elif self.now_status == GameStatus.GAMEOVER:
            pass

        pass

App()
