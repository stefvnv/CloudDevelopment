class Single:

    def __init__(self, val1):
        self._value1 = val1

    def incrValue1(self):
        self._value1 += 1

    def getValue1(self):
        return self._value1


#Extended Class
class Pair(Single):
    def __init__(self, val1, val2):
        super().__init__(val1)
        self.value2 = val2

    def incrValue2(self):
        self.value2 += 1

    def getValue2(self):
        return self.value2

    def add(self):
        return self._value1 + self.value2

    def multiply(self):
        return self._value1 * self.value2

