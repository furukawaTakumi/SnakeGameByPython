import pyxel
from screen.ScreenCreator import CreateStartScreen
from GameStatus import GameStatus
from game_contents.SnakeBody import SnakeBody

resourse_path = "asset/course.pyxres"


class App:
    def __init__(self):
        pyxel.init(130, 90)
        pyxel.mouse(True)
        pyxel.load(resourse_path)
        self.sna = SnakeBody()
        self.now_status = GameStatus.START
        self.startScreen = CreateStartScreen()
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        self.sna.draw()
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
