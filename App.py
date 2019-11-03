import pyxel
from screen.ScreenCreator import CreateStartScreen
from GameStatus import GameStatus
from game_contents.GameController import GameController

resourse_path = "asset/course.pyxres"

class App:
    def __init__(self):
        pyxel.init(130, 90,border_width=4, fps=30)
        pyxel.mouse(True)
        pyxel.load(resourse_path)
        self.now_status = GameStatus.START
        self.startScreen = CreateStartScreen()
        self.gameController = GameController()
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        if self.now_status == GameStatus.GAME:
            self.gameController.UpdateData()
        pass

    def draw(self):
        pyxel.cls(0)

        if self.now_status == GameStatus.START:
            self.startScreen.ScreenUpdate()
            if self.startScreen.isBtnClicked():
                self.now_status = GameStatus.GAME
                pyxel.mouse(False)

        elif self.now_status == GameStatus.GAME:
            self.gameController.UpdateDisplay()

        elif self.now_status == GameStatus.GAMEOVER:
            pass

        pass

App()
