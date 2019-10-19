
from .Feed import Feed

class Parcel:
    def __init__(self):
        self.__object = None

    @property
    def object(self):
        return self.__object

    @object.setter
    def object(self, new_obj):
        self.__object = new_obj

    def CreateFeed(self):
        self.__object = Feed()

    def CreatePoisonFeed(self):
        self.__object = Feed(True)

    def HasFeed(self):
        if self.__object == None:
            return False
        return True
