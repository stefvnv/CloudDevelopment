class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.min = m
        self.sec = s

    def printTime(self):
        print('{0}:{1}:{2}'.format(self.hour, self.min, self.sec))

    def __add__(self, other):
        result = Time(self.hour + other.hour, self.min + other.min, self.sec + other.sec)
        if result.sec > 59:
            result.sec -= 60
            result.min += 1

        if result.min > 59:
            result.min -= 60
            result.hour += 1
        return result

    def __gt__(self, other):
        total1 = self.hour * 60 + self.min * 60 + self.sec
        total2 = other.hour * 60 + other.min * 60 + self.sec
        if total1 > total2:
            return True
        else:
            return False


def main():
    t1 = Time(2, 45, 58)
    t2 = Time(5, 50, 22)
    t3 = Time(6, 22, 42)
    res1 = t1 + t2
    print('\n2:45:58 + 5:50:22= ', end='')
    res1.printTime()

    if t1 > t2:
        print('\n2:45:58 > 5:50:22')

    if t3 > t2:
        print('\n6:22:42 > 5:50:22')


main()
