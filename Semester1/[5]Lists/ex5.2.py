def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = addOdd(list1)
    print('The sum of odd elements in list is {0}.'.format(result))


def addOdd(listp):
    result = 0
    for el in listp:
        if el % 2 == 1:
            result = result + el
    return result


main()
