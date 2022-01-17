def main():
    width = int(input('Enter Width: '))
    display(width)


def display(width):
    for value in range(1, width + 1):
        print('* ', end='')


main()
