def main():
    list1 = [2, 6, 2, 7, 8, 4, 2, 6]
    result = allEven(list1)
    print('All Element Even List 1 =  {0} '.format(result))

    list2 = [2, 6, 2, 8, 8, 4, 2, 6]
    result = allEven(list2)
    print('All Element Even List 2 =  {0} '.format(result))


def allEven(listp):
    result = True

    for el in listp:
        if el % 2 == 1:
            result = False
    return result


main()
