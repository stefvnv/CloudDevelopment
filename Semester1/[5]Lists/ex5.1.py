def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = countEven(list1)
    print('The number of even elements in list is {0}.'.format(result))


def countEven(listp):
    result = 0
    for el in listp:
        if el % 2 == 0:
            result = result + 1
    return result


main()
