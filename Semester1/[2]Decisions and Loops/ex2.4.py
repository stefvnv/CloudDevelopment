def main():
    count = 0
    result = 0

    while count < 5:
        value = int(input('Enter value {0}: '.format(count + 1)))
        result = result + value
        count = count + 1

    print('The sum of the 5 values you entered is {0}'.format(result))


main()
