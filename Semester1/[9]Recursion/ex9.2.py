def countDigits(number):
    if number < 10:
        return 1
    else:
        rest = int(number / 10)
        return 1 + countDigits(rest)


def main():
    x = int(input('Enter number: '))
    result = countDigits(x)
    print('\nResult = {0}'.format(result))


main()
