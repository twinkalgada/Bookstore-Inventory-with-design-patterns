import unittest
from Inventory import Inventory
from Book import Book


class InventoryTest(unittest.TestCase):

    def test_add_book(self):
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":100, "qty":1}')

    def test_sell_book(self):
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        inventory.sell_book(book)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":100, "qty":0}')

    def test_update_price(self):
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        book_updated = Book(name="Two Tales", price="500", qty=1, id=1)
        inventory.update_price(book_updated)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":500, "qty":1}')

    def test_update_qty(self):
        inventory = Inventory()
        book = Book(name="Two Tales", price="100", qty=1, id=1)
        inventory.add_book(book)
        book_updated = Book(name="Two Tales", price="100", qty=5, id=1)
        inventory.update_qty(book_updated)
        self.assertEqual(str(inventory), '{"id":1, "name":"Two Tales", "price":100, "qty":5}')

    def test_get_book_by_name(self):
        inventory = Inventory()
        book_name = 'Two Tales'
        book = Book(name=book_name, price="100", qty=1, id=1)
        inventory.add_book(book)
        book_found = inventory.get_book(book_name=book_name)
        self.assertEqual(str(book_found), '{"id":1, "name":"Two Tales", "price":100, "qty":1}')

    def test_get_book_by_id(self):
        inventory = Inventory()
        book_id = 10
        book = Book(name='Two Tales', price="100", qty=1, id=book_id)
        inventory.add_book(book)
        book_found = inventory.get_book(book_id=book_id)
        self.assertEqual(str(book_found), '{"id":10, "name":"Two Tales", "price":100, "qty":1}')

    def test_book_not_found(self):
        inventory = Inventory()
        book_name = 'Two Tales'
        book = Book(name=book_name, price="100", qty=1, id=1)
        book_found = inventory.get_book(book_name=book_name)
        inventory.add_book(book)
        self.assertEqual(book_found, False)


if __name__ == '__main__':
    unittest.main()
