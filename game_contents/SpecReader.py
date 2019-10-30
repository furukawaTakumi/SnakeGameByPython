
class SpecReader():
    def __init__(self, file_name):
        self.__spec = {}

        with open("../asset/" + file_name, mode="r") as reader:
            lines = reader.readlines()
            for line in lines:
                key = line.split(',')[0]
                val_type = line.split(',')[1]
                val = line.split(',')[2]
                if val_type == "int":
                    self.__spec[key] = int(val)
                elif val_type == "str":
                    self.__spec[key] = val.split('\n')[0]
                else:
                    raise Exception("such value type dose not exists!")

    @property
    def spec(self):
        return self.__spec
