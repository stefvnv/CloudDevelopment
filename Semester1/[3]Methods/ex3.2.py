def main():
    val1 = int(input('Enter Value: '))
    result = sigma(val1)
    print('Sigma {0} = {1}'.format(val1, result))


def sigma(x):
    result = 0
    for value in range(1, x + 1):
        result = result + value
    return result


main()
