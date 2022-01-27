class Data:
    def __init__(self, val1, val2):
        self._value1 = val1
        self._value2 = val2

    def add(self):
        return 0

    def printData(self):
        print('Data= ', self._value1, ':', self._value2, end='')


class Pair(Data):
    def __init__(self, val1, val2):
        super().__init__(val1, val2)

    def add(self):
        return self._value1 + self._value2

    def printData(self):
        super().printData()


class Treble(Data):
    def __init__(self, val1, val2, val3):
        super().__init__(val1, val2)
        self._value3 = val3

    def add(self):
        return self._value1 + self._value2 + self._value3

    def printData(self):
        super().printData()
        print(':', self._value3, end='')


class Quad(Data):
    def __init__(self, val1, val2, val3, val4):
        super().__init__(val1, val2)
        self._value3 = val3
        self._value4 = val4

    def add(self):
        return self._value1 + self._value2 + self._value3 + self._value4

    def printData(self):
        super().printData()
        print(':', self._value3, ':', self._value4, end='')


def main():
    obj1 = Data(2, 3)
    obj2 = Pair(3, 4)
    obj3 = Treble(4, 5, 6)
    obj4 = Quad(5, 6, 7, 8)
    list = [obj1, obj2, obj3, obj4]
    for el in list:
        print('---------')
        el.printData()
        print('\nSum = ', el.add())


main()
