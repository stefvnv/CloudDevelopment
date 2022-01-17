class User:
    def __init__(self, name, day, month, chinese, year, sign1, sign2):
        self.__name = name
        self.__day = day
        self.__month = month
        self.__chinese = chinese
        self.__year = year
        self.__sign1 = sign1
        self.__sign2 = sign2

    def getName(self):
        return self.__name

    def getDay(self):
        return self.__day

    def getMonth(self):
        return self.__month

    def getYear(self):
        return self.__year

    def getChinese(self):
        return self.__chinese

    def getAstrologySign(self):
        return self.__sign1

    def setAstrologySign(self, sign):
        self.__sign1 = sign

    def getChineseSign(self):
        return self.__sign2
