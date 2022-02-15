"""LINEAR/SEQUENTIAL SEARCH"""


class MyList:

    def __init__(self, list):
        self._list = list

    def linearSearch(self, target):
        result = False

        for i in range(0, len(self._list)):
            if self._list[i] == target:
                result = True

        return result

    def readList(self):
        list = ' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list
