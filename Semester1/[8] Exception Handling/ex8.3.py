class IndexTooHigh(Exception):
    pass


class IndexTooLow(Exception):
    pass


def readValue(list, index):
    if index < 0:
        raise IndexTooLow

    if index >= len(list):
        raise IndexTooHigh

    value1 = list[index]
    return value1


def main():
    index = int(input("Enter Index: "))
    list = [1, 4, 5, 6, 4]
    try:
        result1 = readValue(list, index)
        print('Result1 = {0}'.format(result1))

    except IndexTooLow:
        print('Index is too low')

    except IndexTooHigh:
        print('Index is too high')


main()
