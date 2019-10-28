
class SpecReader():
    def __init__(self, file_path):
        self.__spec = {}

        with open(file_path, mode="r") as reader:
            lines = reader.readlines()
            for line in lines:
                key = line.split(',')[0]
                val = line.split(',')[1]
                self.__spec[key] = val

    @property
    def spec(self):
        return self.__spec
