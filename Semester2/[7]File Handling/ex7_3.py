def main():
    infile = open('input3.txt', "r")
    outfile = open('output3.txt', "w")
    highest = 0
    print('Highest Overall Mark (CA + Exam) =: ', file=outfile, end='')

    for line in infile:
        list0 = line.split(' ')
        nextca = int(list0[0])
        nextExam = int(list0[1])
        overall = nextca + nextExam

        if overall > highest:
            highest = overall

    print(highest, file=outfile)


main()
