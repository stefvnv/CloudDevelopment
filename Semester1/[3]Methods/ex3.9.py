def main():
    width = int(input('Enter Width: '))
    display(width)


def display(width):
    for val1 in range(width):
        for val2 in range(width):
            print(' * ', end='')
        print()


main()
