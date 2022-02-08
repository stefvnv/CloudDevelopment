class Money:

    def __init__(self, e, c):
        self.euro = e
        self.cent = c

    def readMoney(self):
        return '€' + str(self.euro) + '.' + str(self.cent)

    def updateMoney(self, e, c):
        self.euro = e
        self.cent = c

    def __add__(self, other):
        result = Money(self.euro + other.euro, self.cent + other.cent)
        if result.cent > 99:
            result.euro += 1
            result.cent -= 100
        return result


class Book:

    def __init__(self, title, author, priceEuro, priceCent, deliveryEuro, deliveryCent):
        self._title = title
        self._author = author
        self._price = Money(priceEuro, priceCent)
        self._delivery = Money(deliveryEuro, deliveryCent)

    def readTitle(self):
        return self._title

    def updateTitle(self, title):
        self._title = title

    def updatePrice(self, euro, cent):
        self._price.updateMoney(euro, cent)

    def updateDelivery(self, euro, cent):
        self._delivery.updateMoney(euro, cent)

    def readAuthor(self):
        return self._author

    def readPrice(self):
        return self._price.readMoney()

    def readDelivery(self):
        return self._delivery.readMoney()

    def totalCost(self):
        total = self._price + self._delivery
        return total.readMoney()
