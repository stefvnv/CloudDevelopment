class Lecturer:

    def __init__(self, name, office):
        self._lect_name = name
        self._office = office

    def getName(self):
        return self._lect_name

    def getOffice(self):
        return self._office

    def updateOffice(self, office):
        self._office = office


class Module:

    def __init__(self, title, topic, lecturerName, office):
        self._title = title
        self._topic = topic
        self._lecturer = Lecturer(lecturerName, office)

    def readTitle(self):
        return self._title

    def updateTitle(self, title):
        self._title = title

    def readTopic(self):
        return self._topic

    def readLecturerName(self):
        return self._lecturer.getName()

    def readLecturerOffice(self):
        return self._lecturer.getOffice()

    def updateLecturerOffice(self, office):
        self._lecturer.updateOffice(office)

