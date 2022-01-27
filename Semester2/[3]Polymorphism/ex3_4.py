class Shape:
    def __init__(self, width):
        self._width = width

    def readType(self):
        return 'Base Shape'

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, width):
        super().__init__(width)

    def readType(self):
        return 'Square '

    def area(self):
        return self._width * self._width


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        self._height = height

    def readType(self):
        return 'Rectangle'

    def area(self):
        return self._width * self._height


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width)
        self._height = height

    def readType(self):
        return 'Triangle '

    def area(self):
        return (self._width * self._height) / 2


def main():
    obj1 = Square(5)
    obj2 = Rectangle(5, 6)
    obj3 = Triangle(5, 6)
    list = [obj1, obj2, obj3]
    for el in list:
        print('\nType =', el.readType())
        print('Area =', el.area())


main()
