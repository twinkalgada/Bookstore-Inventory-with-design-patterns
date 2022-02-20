import unittest
from Inventory import Inventory
from Book import Book
from Commands.AddBook import AddBook
from Commands.SellBook import SellBook
from Commands.UpdatePrice import UpdatePrice
from Commands.UpdateQty import UpdateQty
from LogCommands import LogCommands


class DecoratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.command_log_file = 'CommandLogTest.txt'

    def test_add_book_command_with_decorator(self):
        open(self.command_log_file, 'w').close()  # This will empty the file
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        add_book = AddBook(inventory)   # Command class
        log_commands = LogCommands(add_book)    # Decorator
        result = log_commands.execute(book, self.command_log_file)
        self.assertEqual(result, True)  # Check if it executed the command
        self.assertEqual(str(inventory),
                         '{"id":1, "name":"Two Tales", "price":100, "qty":1}')  # Check if inventory has the book
        file = open(self.command_log_file, 'r')
        lines = file.readlines()
        file.close()
        # Since we emptied the file first it just has one line
        self.assertEqual(lines[0].strip(),
                         '{"command":"add", "book":{"id":1, "name":"Two Tales", "price":100, "qty":1}}')

    def test_sell_book_command_with_decorator(self):
        open(self.command_log_file, 'w').close()  # This will empty the file
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        sell_book = SellBook(inventory) # Command class
        log_commands = LogCommands(sell_book)   # Decorator
        inventory.add_book(book)
        result = log_commands.execute(book, self.command_log_file)
        self.assertEqual(result, True)  # Check if it executed the command
        self.assertEqual(str(inventory),
                         '{"id":1, "name":"Two Tales", "price":100, "qty":0}')  # Check if inventory has the book
        file = open(self.command_log_file, 'r')
        lines = file.readlines()
        file.close()
        # Since we emptied the file first it just has one line
        self.assertEqual(lines[0].strip(),
                         '{"command":"sell", "book":{"id":1, "name":"Two Tales", "price":100, "qty":0}}')

    def test_update_price_command_with_decorator(self):
        open(self.command_log_file, 'w').close()  # This will empty the file
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        update_price = UpdatePrice(inventory)   # Command class
        log_commands = LogCommands(update_price)    # Decorator
        book_updated = Book(name="Two Tales", price="500", qty=1, id=1)
        result = log_commands.execute(book_updated, self.command_log_file)
        self.assertEqual(result, True)  # Check if it executed the command
        self.assertEqual(str(inventory),
                         '{"id":1, "name":"Two Tales", "price":500, "qty":1}')  # Check if inventory has the book
        file = open(self.command_log_file, 'r')
        lines = file.readlines()
        file.close()
        # Since we emptied the file first it just has one line
        self.assertEqual(lines[0].strip(),
                         '{"command":"update_price", "book":{"id":1, "name":"Two Tales", "price":500, "qty":1}}')

    def test_update_qty_command_with_decorator(self):
        open(self.command_log_file, 'w').close()  # This will empty the file
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        update_qty = UpdateQty(inventory)   # Command class
        log_commands = LogCommands(update_qty)  # Decorator
        book_updated = Book(name="Two Tales", price="100", qty=5, id=1)
        result = log_commands.execute(book_updated, self.command_log_file)
        self.assertEqual(result, True)  # Check if it executed the command
        self.assertEqual(str(inventory),
                         '{"id":1, "name":"Two Tales", "price":100, "qty":5}')  # Check if inventory has the book
        file = open(self.command_log_file, 'r')
        lines = file.readlines()
        file.close()
        # Since we emptied the file first it just has one line
        self.assertEqual(lines[0].strip(),
                         '{"command":"update_qty", "book":{"id":1, "name":"Two Tales", "price":100, "qty":5}}')


if __name__ == '__main__':
    unittest.main()
