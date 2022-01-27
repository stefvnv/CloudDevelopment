def main():
    value1 = int(input('Enter Value 1: '))
    value2 = int(input('Enter Value 2: '))
    value3 = int(input('Enter Value 3: '))
    result = largest(value1, value2, value3)
    print('{0} is largest of 3 valued of {1},{2},{3}'.format(result, value1, value2, value3))


def largest(val1, val2, val3):
    if (val1 > val2) and (val1 > val3):
        result = val1
    elif (val2 > val1) and (val2 > val3):
        result = val2
    elif (val3 > val1) and (val3 > val2):
        result = val3
    return result


main()
