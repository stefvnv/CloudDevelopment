def main():

    name = input('Enter your name: ')
    number = int(input('Enter number of times to print the name: '))

    i = 1
    for value in range (0, number):
        print(str(i) + '. Name = {0}'.format(name))
        i = i + 1


main()
