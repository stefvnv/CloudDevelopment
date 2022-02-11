def main():
    infile = open('input4.txt', "r")
    outfile = open('output4.txt', "w")
    line0 = infile.readline()
    line1 = infile.readline()
    lowest = 999
    nameLowest = ''
    print('Name of Person with Lowest Overall Mark (CA + Exam) =: ', file=outfile, end='')

    for line in infile:
        list0 = line.split(' ')
        nextName = list0[0]
        nextca = int(list0[1])
        nextExam = int(list0[2])
        overall = nextca + nextExam

        if overall < lowest:
            lowest = overall
            nameLowest = nextName

    print(nameLowest, file=outfile)


main()
