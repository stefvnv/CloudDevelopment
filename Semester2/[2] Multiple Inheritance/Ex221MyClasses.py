class Single:

    def __init__(self, val1):
        self._value1 = val1

    def incrValue1(self):
        self._value1 += 1

    def getValue1(self):
        return self._value1


# Extended Class

class Pair:

    def __init__(self, val2, val3):
        self._value2 = val2
        self._value3 = val3

    def incrValue2(self):
        self._value2 += 1

    def getValue2(self):
        return self._value2

    def incrValue3(self):
        self._value3 += 1

    def getValue3(self):
        return self._value3


# class Treble goes here
class Treble (Single, Pair):
    def __init__(self, val1, val2, val3):
        Single.__init__(self, val1)
        Pair.__init__(self, val2, val3)

    def add(self):
        return self._value1 + self._value2 + self._value3

    def multiply(self):
        return self._value1 * self._value2 * self._value3
