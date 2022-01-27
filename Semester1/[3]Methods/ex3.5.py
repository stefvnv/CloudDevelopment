def main():
    base = int(input('Enter Base: '))
    pow = int(input('Enter Power: '))
    result = power(base, pow)
    print('{0} to Power of {1} = {2}'.format(base, pow, result))


def power(b, p):
    result = 1
    index = 1
    while index <= p:
        result = result * b
        index = index + 1
    return result


main()
