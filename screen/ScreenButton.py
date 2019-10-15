import pyxel

class ScreenButton:
    def __init__(self, button_struct, position):
        self.size = button_struct.size
        self.colors = button_struct.back_cols
        self.pos = position
        self.text = (button_struct.name, button_struct.name_col)
        pass

    def __isOnMouse(self):
        judge = True
        if self.pos[0] > pyxel.mouse_x:
            judge = False
        if self.pos[0] + self.size[0] < pyxel.mouse_x:
            judge = False
        if self.pos[1] > pyxel.mouse_y:
            judge = False
        if self.pos[1] + self.size[1] < pyxel.mouse_y:
            judge = False
        if judge == True:
            pyxel.rect(self.pos[0], self.pos[1], self.size[0],self.size[1], self.colors[0])
        else:
            pyxel.rect(self.pos[0]-1, self.pos[1], self.size[0],self.size[1], self.colors[1])
        pyxel.text(self.pos[0], self.pos[1], self.text[0], self.text[1])
        return judge

    def isClicked(self):
        if self.__isOnMouse():
            if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                return True
        return False
