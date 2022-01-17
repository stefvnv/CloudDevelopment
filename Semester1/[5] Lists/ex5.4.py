def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]

    lower = int(input('Enter Lower Limit: '))
    upper = int(input('Enter Upper Limit: '))
    result = addInRange(list1, lower, upper)
    print('{0} is sum of elements between {1} and {2}'.format(result, lower, upper))


def addInRange(listp, low, high):
    result = 0

    for el in listp:
        if low <= el <= high:
            result = result + el
    return result


main()
