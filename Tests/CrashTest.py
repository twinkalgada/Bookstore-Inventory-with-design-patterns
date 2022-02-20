import unittest
import json
import shutil
from Inventory import Inventory
from Book import Book
from Commands.AddBook import AddBook
from Commands.SellBook import SellBook
from Commands.UpdatePrice import UpdatePrice
from Commands.UpdateQty import UpdateQty
from LogCommands import LogCommands


def update_inventory_from_commands(inventory, filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        data = json.loads(line.strip())
        command = data['command']
        book_json = data['book']
        book = Book(book_json['name'], book_json['price'], book_json['qty'], book_json['id'])
        if command == 'add':
            inventory.add_book(book)
        if command == 'sell':
            inventory.sell_book(book)
        if command == 'update_price':
            inventory.update_price(book)
        if command == 'update_qty':
            inventory.update_qty(book)
    file.close()
    return inventory


def update_inventory_from_memento(inventory, filename):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        data = json.loads(line.strip())
        book = Book(data['name'], data['price'], data['qty'], data['id'])
        inventory.add_book(book)
    file.close()
    return inventory


class CrashTest(unittest.TestCase):
    def setUp(self) -> None:
        self.snapshot_file = 'SnapshotTest.txt'
        self.command_log_file = 'CommandLogTest.txt'
        self.command_log_file_copy = 'CommandLogTestCopy.txt'

    def test_crash_system(self):
        inventory = Inventory()
        open(self.snapshot_file, 'w').close()  # This will empty the file
        open(self.command_log_file, 'w').close()  # Empty file
        open(self.command_log_file_copy, 'w').close()  # Empty file

        # Write to command file to create a test file
        book_python = Book(name='Python', price=100, qty=10)
        book_java = Book(name='Java', price=300, qty=10)
        book_c = Book(name='C', price=400, qty=10)

        # AddBook
        add_book = AddBook(inventory)
        log_command = LogCommands(add_book)
        log_command.execute(book_python, self.command_log_file)
        log_command.execute(book_java, self.command_log_file)
        log_command.execute(book_c, self.command_log_file)

        # Update Price
        book_python = Book(name='Python', price=500, qty=10)
        update_price = UpdatePrice(inventory)
        log_command = LogCommands(update_price)
        log_command.execute(book_python, self.command_log_file)

        # Update Qty
        book_java = Book(name='Java', price=300, qty=0)
        update_qty = UpdateQty(inventory)
        log_command = LogCommands(update_qty)
        log_command.execute(book_java, self.command_log_file)

        # Sell Book
        book_c = Book(name='C', price=400, qty=1)
        sell_book = SellBook(inventory)
        log_command = LogCommands(sell_book)
        log_command.execute(book_c, self.command_log_file)

        # Create memento
        inventory.save_state(self.snapshot_file)

        # Create copy of command file for reference later
        shutil.copy(self.command_log_file, self.command_log_file_copy)

        # Delete commands from file after memento is created
        open(self.command_log_file, 'w').close()

        # Add some more commands
        # Sell book again
        log_command.execute(book_c, self.command_log_file)

        # Create new instance of Inventory and begin system restore
        inventory_new = Inventory()

        # Update Inventory from memento
        inventory_new = update_inventory_from_memento(inventory_new, self.snapshot_file)

        # Update Inventory from commands
        inventory_new = update_inventory_from_commands(inventory_new, self.command_log_file)

        # Do some more operations on the inventory without registering commands
        inventory_new.sell_book(book_c)

        self.assertEqual(str(inventory_new),
                         '{"id":1, "name":"Python", "price":500, "qty":10},{"id":2, "name":"Java", "price":300, '
                         '"qty":0},{"id":3, "name":"C", "price":400, "qty":0}')


if __name__ == '__main__':
    unittest.main()
