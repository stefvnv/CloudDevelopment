#Enter Value 1: 8
#Enter Value 2: 9
#The largest value is: 9

def main():
    first = int(input('Enter the first price: '))
    second = int(input('Enter the second price: '))
    if first > second:
        print('The largest value is: ', first)
    else:
        print('The largest value is: ', second)

main()

