import pyxel
from screen.ScreenDirector import ScreenDirector
from screen.StartScreenBuilder import StartScreenBuilder
from screen.GameOverScreenBuilder import GameOverScreenBuilder
from GameStatus import GameStatus
from game_contents.GameController import GameController

resourse_path = "assets/course.pyxres"

class App:
    def __init__(self):
        pyxel.init(130, 90,border_width=4, fps=30)
        pyxel.mouse(True)
        pyxel.load(resourse_path)
        self.now_status = GameStatus.START

        # 画面の生成
        startScreenBuilder = StartScreenBuilder()
        director = ScreenDirector(startScreenBuilder)
        director.build()
        self.startScreen = startScreenBuilder.GetBuildInstance()
        self.startScreen.PrepareDisplay()

        gameoverScreenBuilder = GameOverScreenBuilder()
        director = ScreenDirector(gameoverScreenBuilder)
        director.build()
        self.gameoverScreen = gameoverScreenBuilder.GetBuildInstance()

        self.gameController = GameController()

        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        if self.now_status == GameStatus.START:
            if self.startScreen.isBtnClicked("Start!"):
                self.now_status = GameStatus.GAME
                pyxel.mouse(False)

        elif self.now_status == GameStatus.GAME:
            self.gameController.UpdateData()
            if self.gameController.CheckGameOver():
                self.gameoverScreen.PrepareDisplay()
                self.now_status = GameStatus.GAMEOVER

        elif self.now_status == GameStatus.GAMEOVER:
            pyxel.mouse(True)
            if self.gameoverScreen.isBtnClicked("Restart?"):
                self.gameController = GameController()

                self.now_status = GameStatus.GAME
                pyxel.mouse(False)

            elif self.gameoverScreen.isBtnClicked("toTitle"):
                self.gameController = GameController()

                self.gameoverScreen.PrepareDisplay()
                self.startScreen.PrepareDisplay()

                self.now_status = GameStatus.START
                pyxel.mouse(True)
        pass

    def draw(self):
        pyxel.cls(0)

        if self.now_status == GameStatus.START:
            self.startScreen.ScreenUpdate()

        elif self.now_status == GameStatus.GAME:
            self.gameController.UpdateDisplay()

        elif self.now_status == GameStatus.GAMEOVER:
            self.gameoverScreen.ScreenUpdate()


if __name__ == "__main__":
    App()
