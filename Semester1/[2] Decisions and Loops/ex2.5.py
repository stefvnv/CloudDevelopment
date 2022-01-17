def main():
    value = 65
    print(' Ascii Table')
    print('-------------')
    print('Letter      Ascii')

    while value < 75:
        letter = chr(value)
        print('  {0}           {1}'.format(letter, value))
        value = value + 1


main()
