def main():
    infile = open('input2.txt', "r")
    age = 0
    print('Oldest Age: ', end='')
    for line in infile:
        line = line.rstrip()
        list = line.split(' ')
        nextAge = int(list[1])
        if nextAge > age:
            age = nextAge
    print(age)


main()
