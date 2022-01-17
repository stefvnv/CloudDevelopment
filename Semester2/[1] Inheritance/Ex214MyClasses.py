class Stepper:

    def __init__(self, val):
        self._value = val

    def stepDown(self, amount):
        if amount <= self._value:
            self._value -= amount
            return True
        else:
            return False

    def getValue(self):
        return self._value


# Extended Class
class MyStepper(Stepper):

    def __init__(self, value, limit):
        super().__init__(value)
        self.__limit = limit

    def stepUp(self, amount):
        if amount + self._value <= self.__limit:
            self._value += amount
            return True
        else:
            return False

    def getLimit(self):
        return self.__limit

    def resetLimit(self, limit):
        self.__limit = limit
