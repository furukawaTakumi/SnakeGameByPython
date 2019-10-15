class ButtonStruct:
    def __init__(self):
        self.__name = ""
        self.__name_col = 0
        self.__size = 0
        self.__back_cols = (0, 0)

    @property
    def name(self):
        return self.__name

    @property
    def name_col(self):
        return self.__name_col

    @property
    def size(self):
        return self.__size

    @property
    def back_cols(self):
        return self.__back_cols

    @name.setter
    def name(self, name):
        self.__name = name
        self.__size = (len(name) * 4, 5)

    @name_col.setter
    def name_col(self, col):
        self.__name_col = col

    @back_cols.setter
    def back_cols(self, back_cols):
        self.__back_cols = back_cols


class TextStruct:
    def __init__(self, name="", col=0):
        self.__name = name
        self.__length = len(self.__name)
        self.__size = (self.__length * 4, 5)

        self.__col = col
        pass

    @property
    def name(self):
        return self.__name

    @property
    def col(self):
        return self.__col

    @property
    def length(self):
        return self.__length

    @property
    def size(self):
        return self.__size

    @name.setter
    def name(self, name):
        self.__name = name
        self.__length = len(name)
        self.__size = (4 * self.__length, 5)

    @col.setter
    def col(self, col):
        self.__col = col
