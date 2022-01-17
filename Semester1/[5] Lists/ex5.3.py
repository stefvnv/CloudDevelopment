def main():
    list1 = [2, 5, 2, 8, 7, 3, 2, 5]
    target = int(input('Enter Target: '))
    result = countTarget(list1, target)
    print('{0} occurs in list {1} time(s)'.format(target, result))


def countTarget(listp, tar):
    result = False
    for el in listp:
        if el == tar:
            result = True
    return result


main()
