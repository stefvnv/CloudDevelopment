class Product:
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getPrice(self):
        return self.__price

    def readType(self):
        return "Basic Product"

    def readDescription(self):
        return ""


class Car(Product):
    def __init__(self, make, model, price, engine):
        super().__init__(make, model, price)
        self.__engine = engine

    def readType(self):
        return "Basic Product"

    def readDescription(self):
        return "CC= " + str(self.__engine)


class Laptop(Product):
    def __init__(self, make, model, price, ram):
        super().__init__(make, model, price)
        self.__ram = ram

    def readType(self):
        return "Basic Product"

    def readDescription(self):
        return "RAM(GB)= " + str(self.__ram)


class TV(Product):
    def __init__(self, make, model, price, screen):
        super().__init__(make, model, price)
        self.__screen = screen

    def readType(self):
        return "Basic Product"

    def readDescription(self):
        return "Screen(inch)= " + str(self.__screen)
