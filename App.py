import pyxel
import screen.ScreenButton as sb

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.start_btn = sb.ScreenButton((30,10), (1,9),(80,60),("Start!", 7))
        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        if self.start_btn.isClicked():
            pyxel.play(0, 0, loop=False)
        pass

App()
