from Commands.ICommand import ICommand


class SellBook(ICommand):

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return "\"command\":\"sell\""

    def execute(self, book):
        # Execute sell book function of inventory class
        book_sold = self.inventory.sell_book(book)
        return book_sold
