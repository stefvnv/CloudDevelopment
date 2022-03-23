class Transport:
    def __init__(self, country, company):
        self.__country = country
        self.__company = company

    __dhl_cost = 1000
    __ups_cost = 1235
    __fed_cost = 1433

    def readCountry(self):
        return self.__country

    def readDeliveryCompany(self):
        return self.__company

    def readPrice(self):
        if self.__company == "DHL":
            return self.__dhl_cost
        elif self.__company == "UPS":
            return self.__ups_cost
        elif self.__company == "FED":
            return self.__fed_cost


class Part:
    def __init__(self, name, price, country_of_origin, transport_type):
        # private variables
        self.__name = name
        self.__price = price

        # aggregation variables
        self.__transportation = Transport(country_of_origin, transport_type)

    def readName(self):
        return self.__name

    def readPrice(self):
        return self.__price

    def setPrice(self, newPrice):
        self.__price = newPrice

    '''Aggregation functions'''
    def readTransport(self):
        return self.__transportation.readDeliveryCompany()

    def readPriceExt(self):
        return self.__transportation.readPrice()

    '''Polymorphism'''
    def readDesc1(self):
        return ''

    def readDesc2(self):
        return ''

    def readDesc3(self):
        return ''


class CPU(Part):
    def __init__(self, name, price, country_of_origin, transport_type, cores, base, top):
        super().__init__(name, price, country_of_origin, transport_type,)
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
    def __init__(self, name, price, country_of_origin, transport_type, size, speeds, noise):
        super().__init__(name, price, country_of_origin, transport_type,)
        self.__size = size
        self.__speeds = speeds
        self.__noise = noise

    def readDesc1(self):
        return 'Size: ' + str(self.__size)

    def readDesc2(self):
        return 'Fan Speeds: ' + str(self.__speeds)

    def readDesc3(self):
        return 'Noise Level: ' + str(self.__noise)
