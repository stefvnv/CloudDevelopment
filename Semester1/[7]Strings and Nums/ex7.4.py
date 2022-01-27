from enum import IntEnum


class Shape(IntEnum):
    Add = 1
    Sub = 2
    Mult = 3


def main():
    x = int(input('Enter Value1: '))
    y = int(input('Enter Value2: '))
    print('\nOptions')
    print('-------')
    print('Add: Enter {0}'.format(Shape.Add))
    print('Sub: Enter {0}'.format(Shape.Sub))
    print('Multiply: Enter {0}'.format(Shape.Mult))
    choice = int(input('Enter Choice:'))
    if choice == Shape.Add:
        print("\nResult: ", (x + y))
    elif choice == Shape.Sub:
        print("\nResult: ", (x - y))
    elif choice == Shape.Mult:
        print("\nResult: ", (x * y))


main()
