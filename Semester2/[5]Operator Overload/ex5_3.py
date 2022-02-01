class Height:
    def __init__(self, f, i):
        self.feet = f
        self.inches = i

    def printHeight(self):
        print('{0}\'-{1}\"'.format(self.feet, self.inches))

    def __add__(self, other):
        result = Height(self.feet + other.feet, self.inches + other.inches)
        if result.feet > 12:
            result.inches -= 12
            result.feet += 1
        return result

    def __isub__(self, other):
        total1 = self.feet * 12 + self.inches
        total2 = other.feet * 12 + other.inches
        total3 = total1 - total2
        feet = int(total3 / 12)
        inches = total3 % 12
        return Height(feet, inches)

    def __eg__(self, other):
        total1 = self.feet + self.inches
        total2 = other.feet + other.inches
        if total1 > total2:
            return True
        else:
            return False


def main():
    h1 = Height(5, 10)
    h2 = Height(5, 10)
    h3 = Height(8, 5)
    res1 = h1 + h3
    print('\n5 ft 10 ins + 8 ft 5 ins= ', end='')
    res1.printHeight()

    h3 -= h2
    print('\n 8 ft 1 ins -= 5 ft 9 ins= ', end='')
    h3.printHeight()

    if h1 == h2:
        print('\nBoth 5 ft 10 ins')

    if h1 == h3:
        print('\nBoth are not 5 ft 10 ins')


main()
