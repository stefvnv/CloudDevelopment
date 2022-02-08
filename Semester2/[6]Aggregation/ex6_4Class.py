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

    def setValue(self, val):
        self._value = val


class MyStepper:

    def __init__(self, val, lim):
        self._limit = lim
        self._baseStepper = Stepper(val)

    def stepDown(self, amount):
        return self._baseStepper.stepDown(amount)

    def stepUp(self, amount):
        oldValue = self._baseStepper.getValue()
        if amount + oldValue <= self._limit:
            newValue = oldValue + amount
            self._baseStepper.setValue(newValue)
            return True
        else:
            return False

    def getValue(self):
        return self._baseStepper.getValue()

    def getLimit(self):
        return self._limit

    def resetLimit(self, lim):
        self._limit = lim
