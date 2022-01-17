def main():
    height = int(input('Enter Height: '))
    display(height)


def display(height):
    for value in range(1, height + 1):
        print('*')


main()
