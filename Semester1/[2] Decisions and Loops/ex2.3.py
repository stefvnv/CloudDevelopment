import math

def main():
    val1 = int(input('Enter value 1: '))
    val2 = int(input('Enter value 2: '))

    print('\nEnter \'+\' to ADD')
    print('Enter \'-\' to SUBTRACT')
    print('Enter \'*\' to MULTIPLY')
    option = int(input('Enter Option Choice: '))
    if option == '+':
        result = val1 + val2
        print('The sum of {0}, {1} is {2)'.format((val1, val2, result)))
    elif option (option == '-'):
        print('The subtraction of {0}, {1} is {2)'.format((val1, val2, result)))
    else:
        result = val1 * val2
        print('The multiplication of {0}, {1} is {2)'.format((val1, val2, result)))


main()
