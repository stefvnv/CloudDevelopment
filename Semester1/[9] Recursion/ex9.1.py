def power(base, pow):
    if pow == 0:
        return 1
    else:
        return base * power(base, pow - 1)


def main():
    b = int(input('Enter base: '))
    p = int(input('Enter power: '))
    result = power(b, p)
    print('\nResult = {0}'.format(result))


main()
