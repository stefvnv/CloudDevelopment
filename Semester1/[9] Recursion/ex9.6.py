def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    target = int(input('Enter Target: '))
    result = countTarget(list1, target)
    print('{0} Occurs in List {1} Times'.format(target, result))


def countTarget(listp, tar):
    if len(listp) == 0:
        return 0
    else:
        first = listp.pop(0)
        if tar == first:
            return 1 + countTarget(listp, tar)
        else:
            return 0 + countTarget(listp, tar)


main()
