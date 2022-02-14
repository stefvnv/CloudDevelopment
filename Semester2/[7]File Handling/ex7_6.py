def main():
    infile = open('input6.txt', "r")
    outfile = open('output6.txt', "w")
    line = infile.readline()
    line = infile.readline()
    line = infile.readline()
    line = infile.readline()

    print('Manu Players Total Appearances and Goals Per Game: ', file=outfile)
    print('-------------------------------------------------- ', file=outfile)
    for line in infile:
        line.rstrip()
        list = line.split(' ')
        nextname = list[0]
        list2 = list[1].split('-')
        started = int(list2[0])
        sub = int(list2[1])
        goals = int(list2[2])
        totalAppearances = started + sub
        goalsPerGame = (goals / totalAppearances)
        goalsPerGame = round(goalsPerGame, 2)
        print(nextname, '\t', totalAppearances, '\t', goalsPerGame, file=outfile)


main()
