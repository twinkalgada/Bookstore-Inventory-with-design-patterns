from Memento import Memento
import copy


class Inventory:

    def __init__(self):
        self.book_list = []

    def __str__(self):
        book_str_list = []
        for b in self.book_list:
            text = "{\"id\":" + str(b.id) + ", \"name\":\"" + b.name + "\", \"price\":" + str(
                b.price) + ", \"qty\":" + str(b.qty) + "}"
            book_str_list.append(text)
        result = ','.join(book_str_list)
        return result

    def add_book(self, Book):
        book_in_inventory = self.get_book(Book.name)
        if book_in_inventory:
            self.book_list[self.book_list.index(book_in_inventory)].qty += Book.qty
            return book_in_inventory
        else:
            self.book_list.append(Book)
            return Book

    def update_qty(self, Book):
        book_in_inventory = self.get_book(Book.name)
        if book_in_inventory:
            self.book_list[self.book_list.index(book_in_inventory)].qty = Book.qty
            return book_in_inventory
        return False

    def update_price(self, Book):
        book_in_inventory = self.get_book(Book.name)
        if book_in_inventory:
            self.book_list[self.book_list.index(book_in_inventory)].price = Book.price
            return book_in_inventory
        return False

    def get_book(self, book_name='', book_id=''):
        book_list_by_name = list(filter(lambda Book: Book.name == book_name, self.book_list))
        book_list_by_id = list(filter(lambda Book: Book.id == book_id, self.book_list))
        if book_list_by_id:
            return book_list_by_id[0]
        elif book_list_by_name:
            return book_list_by_name[0]
        else:
            return False

    def sell_book(self, Book):
        book_to_sell = self.get_book(Book.name)
        if book_to_sell:
            self.book_list[self.book_list.index(book_to_sell)].qty -= Book.qty
            return book_to_sell
        return False

    def save_state(self, filename):
        return Memento(copy.deepcopy(self.book_list), filename)
