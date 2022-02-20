import unittest
from Inventory import Inventory
from Book import Book
from Commands.AddBook import AddBook
from Commands.SellBook import SellBook
from Commands.UpdatePrice import UpdatePrice
from Commands.UpdateQty import UpdateQty


class CommandTest(unittest.TestCase):

    def test_add_book_command(self):
        inventory = Inventory()
        add_book = AddBook(inventory)  # command class
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        book_added = add_book.execute(book)
        self.assertEqual(str(book_added), '{"id":1, "name":"Two Tales", "price":100, "qty":1}')

    def test_sell_book_command(self):
        inventory = Inventory()
        add_book = AddBook(inventory)   # Add book first
        sell_book = SellBook(inventory) # command class
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        add_book.execute(book)
        book_sold = sell_book.execute(book)
        self.assertEqual(str(book_sold), '{"id":1, "name":"Two Tales", "price":100, "qty":0}')

    def test_update_price_command(self):
        inventory = Inventory()
        add_book = AddBook(inventory)
        update_price = UpdatePrice(inventory)   # command class
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        add_book.execute(book)
        book_updated = Book(name="Two Tales", price="500", qty=1, id=1)
        update_price.execute(book_updated)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":500, "qty":1}')

    def test_update_qty_command(self):
        inventory = Inventory()
        add_book = AddBook(inventory)
        update_qty = UpdateQty(inventory)   # command class
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        add_book.execute(book)
        book_updated = Book(name="Two Tales", price="100", qty=5, id=1)
        update_qty.execute(book_updated)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":100, "qty":5}')


if __name__ == '__main__':
    unittest.main()
