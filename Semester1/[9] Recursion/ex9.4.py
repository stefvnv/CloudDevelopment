def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    result = countEven(list1)
    print('Number of Even els in list = {0}'.format(result))


def countEven(listp):
    if len(listp) == 0:
        return 0
    else:
        first = listp.pop(0)  # remove first
        if first % 2 == 0:
            return 1 + countEven(listp)
        else:
            return 0 + countEven(listp)


main()
