def main():
    val1 = int(input('Enter value 1: '))
    val2 = int(input('Enter value 2: '))
    val3 = int(input('Enter value 3: '))

    if val1 > val2 and (val1 > val3):
        print('{0} is the largest value.'.format(val1))
    else:
        if val2 > val1 and (val2 > val3):
            print('{0} is the largest value.'.format(val2))
        else:
            print('{0} is the largest value.'.format(val3))

    #OR
    #if val1 > val2 and (val1 > val3):
    #    print('{0} is the largest value.'.format(val1))
    #elif val2 > val1 and (val2 > val3):
    #    print('{0} is the largest value.'.format(val2))
    #else:
    #    print('{0} is the largest value.'.format(val3))

main()