class Money:

    def __init__(self, amount, currency_type):
        self.amount = amount
        self.currency_type = currency_type

    def converter(self):
        if self.currency_type == "USD":
            return self.amount * 1
        if self.currency_type == "JPY":
            return self.amount * .00903135
        if self.currency_type == "EUR":
            return self.amount * 1.11369
        if self.currency_type == "BTC":
            return self.amount * .00187265

    def __str__(self):
        return "{} , {}".format(self.amount, self.currency_type)

    def __eq__(self, other):
        return self.converter() > other.converter()

    def __ne__(self, other):
        return self.converter() != other.converter()

    def __le__(self, other):
        return self.converter() <= other.converter()

    def __lt__(self, other):
        return self.converter() < other.converter()

    def __gt__(self, other):
        return self.converter() > other.converter()

    def __ge__(self, other):
        return self.converter() >= other.converter()

    def __add__(self, other):
        return self.converter() + other.converter()

    def __mul__(self, other):
        return self.converter() * other.converter()

    def __sub__(self, other):
        return self.converter() - other.converter()

USD = Money(50, "USD")
JPY = Money(1000, "JPY")
EUR = Money(25, "EUR")
BTC = Money(5, "BTC")

print("USD >= BTC: ", USD >= BTC)
print("USD < EUR: ", USD < EUR)
print("USD * JPY: ", USD * JPY)
print("USD + BTC: ", USD + BTC)
print("USD - EUR: ", USD - EUR)

print(JPY.converter())
print(EUR.converter())
print(BTC.converter())

