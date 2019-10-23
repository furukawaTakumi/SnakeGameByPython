import pyxel
from screen.ScreenCreator import CreateStartScreen
from GameStatus import GameStatus
from game_contents.Snake import Snake
from game_contents.Field import Field

resourse_path = "asset/course.pyxres"

class App:
    def __init__(self):
        pyxel.init(130, 90,border_width=4, fps=30)
        pyxel.mouse(True)
        pyxel.load(resourse_path)
        self.sna = Snake({"x": 0, "y": 0})
        self.now_status = GameStatus.START
        self.startScreen = CreateStartScreen()
        self.field = Field((16,11))

        self.flag = True

        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        if self.now_status == GameStatus.GAME:
            self.sna.RespondToDirect()
            self.sna.UpdatePosition()

            if pyxel.btn(pyxel.KEY_SPACE) and self.flag:
                self.sna.Growth()
                self.flag = False
        pass

    def draw(self):
        pyxel.cls(0)
        self.field.Draw()

        if self.now_status == GameStatus.START:
            self.startScreen.ScreenUpdate()
            if self.startScreen.isBtnClicked():
                self.now_status = GameStatus.GAME

        elif self.now_status == GameStatus.GAME:
            self.sna.DrawBody()

            pass
        elif self.now_status == GameStatus.GAMEOVER:
            pass

        pass

App()
