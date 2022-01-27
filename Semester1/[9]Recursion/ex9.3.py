def countEven(number):
    if number < 10:
        if number % 2 == 0:
            return 1
        else:
            return 0

    else:
        last = number % 10
        rest = int(number / 10)
        if last % 2 == 0:
            return 1 + countEven(rest)
        else:
            return 0 + countEven(rest)


def main():
    x = int(input('Enter number: '))
    result = countEven(x)
    print('\nResult = {0}'.format(result))


main()
