from Commands.ICommand import ICommand


class UpdateQty(ICommand):

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return "\"command\":\"update_qty\""

    def execute(self, book):
        # Execute update_qty function of inventory class
        book_updated = self.inventory.update_qty(book)
        return book_updated
