import itertools


class Book:
    new_id = itertools.count(start=1)

    def __init__(self, name, price, qty, id=None):
        if id is None:
            self.id = next(Book.new_id)
        else:
            self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def __str__(self):
        return "{\"id\":" + str(self.id) + ", \"name\":\"" + self.name + "\", \"price\":" + str(
            self.price) + ", \"qty\":" + str(self.qty) + "}"
