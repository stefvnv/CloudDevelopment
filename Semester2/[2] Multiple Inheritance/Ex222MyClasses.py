class Programmer:

    def __init__(self, language, level):
        self._language = language
        self._level = level

    def stepProgammingLevel(self):
        self._level += 1

    def getLevel(self):
        return self._level

    def getLanguage(self):
        return self._language


# ---------------------------------------------

class Manager:

    def __init__(self, title, employees):
        self._title = title
        self._employees = employees

    def incrementEmployees(self):
        self._employees += 1

    def getEmployees(self):
        return self._employees

    def getTitle(self):
        return self._title


# Extended Class
class ProgrammingManager(Programmer, Manager):

    def __init__(self, language, level, title, employees):
        Programmer.__init__(self, language, level)
        Manager.__init__(self, title, employees)

    def decrementEmployees(self):
        self._employees -= 1

    def changeTitle(self, newTitle):
        self._title = newTitle
