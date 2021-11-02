# Exercise 1 : Built-In Functions
#
# class Newclass:
#     """This is doc string"""
#     def __init__(self):
#         pass
#
#     def __abs__(self):
#         print("this is absolute")
#
#     def __int__(self):
#         print("this is int")
#
# object1 = Newclass()
# print(Newclass.__doc__)
# print(object1.__doc__)
#
# object1.__abs__()
# object1.__int__()
#
# Exercise 2: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount = self.amount + other
            return self.amount
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self.amount
            else:
                raise Exception("Cannot add between Currency type <dollar> and <shekel>")
        else:
            raise Exception("Cannot add except objects and ints")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
