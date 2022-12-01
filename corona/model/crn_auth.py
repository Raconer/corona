import datetime

class auth:
    
    # pid:int = 0

    def __init__(self):
        self.__id = 0
        self.__pid = 0
        self.__regDate = datetime

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, pid):
        self.__pid = pid

    @property
    def regDate(self):
        return self.__regDate

    @regDate.setter
    def regDate(self, regDate):
        self.__regDate = regDate