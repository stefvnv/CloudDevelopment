class Transport:
    def __init__(self, country, company):
        self.__country = country
        self.__company = company

    __dhl_cost = str(1000)
    __ups_cost = str(1235)
    __fed_cost = str(1433)
    __default_cost = str(0)

    def readCountry(self):
        return self.__country

    def readDeliveryCompany(self):
        return self.__company

    def setCompany(self, compIn):
        self.__company = compIn

    def readCompany(self):
        return self.__company

    def readPrice(self):
        if self.__company == "DHL":
            return self.__dhl_cost
        elif self.__company == "UPS":
            return self.__ups_cost
        elif self.__company == "FedEx":
            return self.__fed_cost
        else:
            return self.__default_cost


class Part:
    def __init__(self, name, price, country_of_origin, transport_company):
        # private variables
        self.__name = name
        self.__price = price

        # aggregation variables
        self.__transportation = Transport(country_of_origin, transport_company)

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

    def setCompanyExt(self, companyName):
        self.__transportation.setCompany(companyName)

    def readCompanyExt(self):
        return self.__transportation.readCompany()

    '''Polymorphism'''

    def readDesc1(self):
        return ''

    def readDesc2(self):
        return ''

    def readDesc3(self):
        return ''


class CPU(Part):
    def __init__(self, name, price, country_of_origin, transport_company, cores, base, top):
        super().__init__(name, price, country_of_origin, transport_company, )
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
    def __init__(self, name, price, country_of_origin, transport_company, size, speeds, noise):
        super().__init__(name, price, country_of_origin, transport_company, )
        self.__size = size
        self.__speeds = speeds
        self.__noise = noise

    def readDesc1(self):
        return 'Size: ' + str(self.__size)

    def readDesc2(self):
        return 'Fan Speeds: ' + str(self.__speeds)

    def readDesc3(self):
        return 'Noise Level: ' + str(self.__noise)
