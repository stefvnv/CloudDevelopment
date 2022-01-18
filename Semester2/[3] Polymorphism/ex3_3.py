class Line:
    def __init__(self, length):
        self._length = length

    def draw(self):
        print('Base Class')


class VertLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print('Vertical Line')
        for i in range(self._length):
            print(' *')


class HorzLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print('Horizontal Line')
        for i in range(self._length):
            print(' * ', end='')
        print()


class SlashLine(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print('Slash Line')
        for i in range(self._length):
            print(' ' * i, end=' * \n')


class Square(Line):
    def __init__(self, length):
        super().__init__(length)

    def draw(self):
        print('Square')
        for i in range(self._length):
            for i in range(self._length):
                print('*', end='  ')
            print()


def main():
    obj1 = VertLine(5)

    obj2 = HorzLine(6)

    obj3 = SlashLine(7)

    obj4 = Square(8)

    list = [obj1, obj2, obj3, obj4]
    for el in list:
        print('')
        el.draw()


main()
