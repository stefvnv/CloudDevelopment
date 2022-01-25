def main():
    studentList = {'Smith': 58, 'Jones': 86, 'Peters': 78, 'Adams': 44, 'Cross': 25}
    lower = int(input('Enter Lower Age: '))
    upper = int(input('Enter Upper Age: '))
    printInRange(studentList, lower, upper)


def printInRange(studentL, low, high):
    print('\nList of Names')
    print('=============')

    for key, value in studentL.items():
        if value >= low and value <= high:
            print(key)


main()
