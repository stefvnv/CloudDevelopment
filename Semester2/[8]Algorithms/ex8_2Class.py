"""BINARY SEARCH"""


class MyList:

    def __init__(self, list):
        self._list = list

    def binarySearch(self, target):
        lower = 0
        upper = len(self._list) - 1
        mid = int((lower + upper) / 2)
        found = False

        while found == False and lower <= upper:

            mid = (lower + upper) // 2

            if target == self._list[mid]:
                return mid
            elif target < self._list[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
        return found

    def readList(self):
        self._list = sorted(self._list)
        list = ' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list
