def main():
    infile = open('input2.txt', "r")
    outfile = open('output2.txt', "w")
    age = 0
    print('Name of oldest person is: ', end='')
    oldest = ''

    for line in infile:
        line = line.rstrip()
        list = line.split(' ')
        nextName = list[0]
        nextAge = int(list[1])
        if nextAge > age:
            age = nextAge
            oldest = nextName
    print(oldest, file=outfile)


main()
