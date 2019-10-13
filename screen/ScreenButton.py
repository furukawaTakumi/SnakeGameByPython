import pyxel

class ScreenButton:
    # size = (width, height)
    # btn_col = (btn_col, btn_col_on_mouse)
    # point = (x,y)
    # text = (str,txt_col)
    def __init__(self, size, btn_col, point, txt):
        self.size = size
        self.colors = btn_col
        self.position = point
        self.text = txt
        pass

    def __isOnMouse(self):
        judge = True
        if self.position[0] > pyxel.mouse_x:
            judge = False
        if self.position[0] + self.size[0] < pyxel.mouse_x:
            judge = False
        if self.position[1] > pyxel.mouse_y:
            judge = False
        if self.position[1] + self.size[1] < pyxel.mouse_y:
            judge = False
        if judge == True:
            pyxel.rect(self.position[0], self.position[1], self.size[0],self.size[1], self.colors[0])
        else:
            pyxel.rect(self.position[0], self.position[1], self.size[0],self.size[1], self.colors[1])
        pyxel.text(self.position[0], self.position[1], self.text[0], self.text[1])
        return judge

    def isClicked(self):
        if self.__isOnMouse():
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                return True
        return False
