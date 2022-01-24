def main():
    set1= {2, 5, 2, 8, 7}
    set2= {1,2,3,4,5}

    result = countBoth(set1,set2)
    print('# Unique Elements found in both sets = {0}'.format( result))

def countBoth(setp1,setp2):
    setp3 = setp1.intersection(setp2)
    result = len(setp3)
    return result

main()
