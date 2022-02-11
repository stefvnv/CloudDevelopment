def main():
    infile = open('input5.txt', "r")
    outfile = open('output5.txt', "w")
    line = infile.readline()
    line = infile.readline()

    print('List of Overall Marks=: ', file=outfile)
    print('----------------------- ', file=outfile)
    for line in infile:


main()
