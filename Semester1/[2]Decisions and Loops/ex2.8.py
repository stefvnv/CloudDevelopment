def main():
    count = 0
    result = 0

    while count < 5:
        value = int(input('Enter Value {0}: '.format(count+1)))
        result = result + value
        count = count + 1
    print('Sum of 5 values = {0}'.format(result))


main()
