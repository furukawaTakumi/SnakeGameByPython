"""
Builderパターンを画面生成に適用する
"""

from abc import ABCMeta, abstractmethod

class ScreenBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.title = None
        self.buttons = []
        pass

    @abstractmethod
    def SettingTitle(self):
        pass

    @abstractmethod
    def SettingButton(self):
        pass