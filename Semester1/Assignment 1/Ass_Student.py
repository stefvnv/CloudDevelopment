class Student:

    def __init__(self, name, ID, International):
        self.__name = name
        self.__ID = ID
        self.__present = 0
        self.__absent = 0
        self.__excused = 0
        self.__International = International

    def getName(self):
        return self.__name

    def getID(self):
        return self.__ID

    def getPresent(self):
        return self.__present

    def getAbsent(self):
        return self.__absent

    def getExcused(self):
        return self.__excused

    def getInternational(self):
        return self.__International

    def getPercentAttendance(self):
        if (self.__present + self.__absent + self.__excused) == 0:
            return 0
        else:
            return int(100 * (self.__present / (self.__present + self.__absent + self.__excused)))

    def markPresent(self):
        self.__present += 1

    def markAbsent(self):
        self.__absent += 1

    def markExcused(self, daysExcused):
        self.__excused += daysExcused
