import unittest
from Inventory import Inventory
from Book import Book


class MementoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.command_log_file = 'CommandLogTest.txt'
        self.snapshot_file = 'SnapshotTest.txt'
        self.inventory = Inventory()
        open(self.command_log_file, 'w').close()  # Empty file
        open(self.snapshot_file, 'w').close()  # Empty file

        # Write to command file to create a test file
        book_python = Book(name='Python', price=100, qty=12)

        # AddBook
        self.inventory.add_book(book_python)

    def test_memento_save(self):
        # Create memento
        self.inventory.save_state(self.snapshot_file)
        file = open(self.snapshot_file, 'r')
        lines = file.readlines()
        self.assertEqual(str(self.inventory), lines[0].strip())
        file.close()


if __name__ == '__main__':
    unittest.main()
