"""SELECTION SORT"""


class MyList:

    def __init__(self, list):
        self._list = list

    def selectionSort(self):
        global minim, i
        pass

        for i in range(len(self._list) - 1):
            minim = i

            for j in range(i + 1, len(self._list) - 1):
                if self._list[minim] > self._list[j]:
                    minim = j

        # Swap
        self._list[i], self._list[minim] = self._list[minim], self._list[i]

    def readList(self):
        list = ' [ '
        for el in self._list:
            list += str(el) + ', '
        list += ']'
        return list
