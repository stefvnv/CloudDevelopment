def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = addOdd(list1)
    print('Sum of Odd els in list = {0}'.format(result))


def addOdd(listp):
    if len(listp) == 0:
        return 0
    else:
        first = listp.pop(0)  # remove first
        if first % 2 == 1:
            return first + addOdd(listp)
        else:
            return 0 + addOdd(listp)


main()
