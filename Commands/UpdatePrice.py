from Commands.ICommand import ICommand


class UpdatePrice(ICommand):

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return "\"command\":\"update_price\""

    def execute(self, book):
        # Execute update_price function of inventory class
        book_updated = self.inventory.update_price(book)
        return book_updated
