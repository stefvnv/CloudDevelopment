def main():
    infile = open('input5.txt', "r")
    outfile = open('output5.txt', "w")
    line = infile.readline()
    line = infile.readline()

    print('List of Overall Marks=: ', file=outfile)
    print('----------------------- ', file=outfile)
    for line in infile:
        line.rstrip()
        list = line.split(' ')
        nextname = list[0]
        list2 = list[1].split(';')
        mark1 = int(list2[0])
        mark2 = int(list2[1])
        mark3 = int(list2[2])
        mark4 = int(list2[2])
        average = int((mark1 + mark2 + mark3 + mark4) / 4)
        print(nextname, '\t', average, file=outfile)


main()
