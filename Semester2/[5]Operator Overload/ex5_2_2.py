class Money:
    def __init__(self, e, c):
        self.euro = e
        self.cent = c

    def printMoney(self):
        print('€{0}.{1}'.format(self.euro, self.cent))

        # Add   __iadd__(self, other): and    __sub__(self, other):

    def __iadd__(self, other):
        result = Money(self.euro + other.euro, self.cent + other.cent)
        if result.cent > 99:
            result.cent -= 100
            result.euro += 1
        return result

    def __sub__(self, other):
        total1 = self.euro * 100 + self.cent
        total2 = other.euro * 100 + other.cent
        total3 = total1 - total2
        euro = int(total3 / 100)
        cent = total3 % 100
        return Money(euro, cent)

    def __gt__(self, other):
        total1 = self.euro * 100 + self.cent
        total2 = other.euro * 100 + other.cent
        if total1 > total2:
            return True
        else:
            return False


def main():
    m1 = Money(2, 43)
    m2 = Money(5, 29)
    m3 = Money(9, 73)

    if m3 > m2:
        print(' M3 is bigger')
    else:
        print(' M3 not bigger')

    res1 = m2 - m1
    print('\n(5.29 - 2.43= ', end='')
    res1.printMoney()
    res2 = m3 - m2
    print('\n (9.73 - 5.29= ', end='')
    res2.printMoney()
    m3 += m1
    print('\n (9.73 += 2.43= ', end='')
    m3.printMoney()


main()
