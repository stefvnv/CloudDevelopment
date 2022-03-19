#class Category:



class Part:
    def __init__(self, name, price):

        # private variables
        self.__name = name
        self.__price = price

        # ADD AGGREGATION - USE ANOTHER CLASS TO ADD CATEGORY

    def readName(self):
        return self.__name

    def readPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice


class CPU(Part):
    def __init__(self, name, price, cores, base, top):
        super().__init__(name, price)
        self.__cores = cores
        self.__base = base
        self.__top = top

    def readDesc1(self):
        return 'Cores/Threads: ' + str(self.__cores)

    def readDesc2(self):
        return 'Base Frequency: ' + str(self.__base)

    def readDesc3(self):
        return 'Top Boost Frequency: ' + str(self.__top)


class CPUCooler(Part):
    def __init__(self, name, price, ):
        super().__init__(name, price)