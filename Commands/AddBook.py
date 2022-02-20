from Commands.ICommand import ICommand


class AddBook(ICommand):

    def __init__(self, inventory):
        self.inventory = inventory

    def __str__(self):
        return "\"command\":\"add\""

    def execute(self, book):
        # Execute add book function of inventory class
        book_added = self.inventory.add_book(book)
        return book_added
