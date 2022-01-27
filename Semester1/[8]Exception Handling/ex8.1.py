def decrement(value1):
    if value1 == 0:
        raise Exception
    else:
        value1 -= 1
        return value1


def main():
    value = int(input("Enter Initial Value: "))

    try:
        result1 = decrement(value)
        print('Result 1: {0}'.format(result1))
        result2 = decrement(result1)
        print('Result 2: {0}'.format(result2))
        result3 = decrement(result2)
        print('Result 3: {0}'.format(result3))

    except:
        print('Value Already 0')


main()
