# ---------------------------------------------

class Student:

    def __init__(self, course, year):
        self._course = course
        self._yearOfStudy = year

    def incrementYear(self):
        self._yearOfStudy += 1

    def getYear(self):
        return self._yearOfStudy

    def getCourse(self):
        return self._course


class Lecturer:

    def __init__(self, topic, teachingHours):
        self._topic = topic
        self._teachingHours = teachingHours

    def getHours(self):
        return self._teachingHours

    def getTopic(self):
        return self._topic

    def setTopic(self, topic):
        self._topic = topic

    # Extended Class


class PostGraduate(Student, Lecturer):

    def __init__(self, course, year, topic, hours, office):
        Student.__init__(self, course, year)
        Lecturer.__init__(self, topic, hours)
        self.__office = office

    def setHours(self, newHours):
        self._teachingHours = newHours

    def getOffice(self):
        return self.__office
