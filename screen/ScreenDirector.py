

class ScreenDirector:
    def __init__(self, builder):
        self.builder = builder
        pass

    def build(self):
        self.builder.SettingTitle()
        self.builder.SettingButton()
        pass