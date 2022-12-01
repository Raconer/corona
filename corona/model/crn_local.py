import datetime

class local:
    def __init__(self):
        self.__idx = 0
        self.__deathCnt = 0
        self.__gubunCn =  ""
        self.__gubunEn =  ""
        self.__isolClearCnt  = 0
        self.__isolIngCnt = 0
        self.__qurRate = 0
        self.__updateDt = datetime
        self.__gubun = ''
        self.__incDec = 0
        self.__localOccCnt = 0
        self.__seq = 0
        self.__defCnt = 0
        self.__overFlowCnt= 0
        self.__stdDay = datetime     
        
    def set_data(self, crn_data):
        self.__deathCnt     = crn_data["deathCnt"]
        self.__gubunCn      = crn_data["gubunCn"]
        self.__gubunEn      = crn_data["gubunEn"]
        self.__isolClearCnt = crn_data["isolClearCnt"]
        self.__isolIngCnt   = crn_data["isolIngCnt"]
        self.__qurRate      = crn_data["qurRate"]
        self.__updateDt     = crn_data["updateDt"]
        self.__gubun        = crn_data["gubun"]
        self.__incDec       = crn_data["incDec"]
        self.__localOccCnt  = crn_data["localOccCnt"]
        self.__seq          = crn_data["seq"]
        self.__defCnt       = crn_data["defCnt"]
        self.__overFlowCnt  = crn_data["overFlowCnt"]
        self.__stdDay       = crn_data["stdDay"]

    @property
    def gubun(self): 
        return self.__gubun
        
    @gubun.setter
    def gubun(self, gubun):
        self.__gubun = gubun