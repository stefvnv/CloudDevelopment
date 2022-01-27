def main():
    val1 = int(input('Enter Value: '))
    val2 = int(input('Enter Value: '))
    result = my_max(val1, val2)
    print('Max = {0}'.format(result))


def my_max(x, y):
    result = 0
    if x > y:
        result = x
    else:
        result = y
    return result


main()
