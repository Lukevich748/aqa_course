
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def get_status(self):
        if self.is_borrowed is True:
            return "Взята"
        else:
            return "Доступна"


book_1 = Book(title="Book 1", author="Author 1")

print(book_1.get_status())
book_1.borrow_book()
print(book_1.get_status())
book_1.return_book()
print(book_1.get_status())
