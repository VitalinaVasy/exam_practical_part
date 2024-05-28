import datetime


class IDGenerator:
    _id = 0

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id


class Book:
    def __init__(self, title, author):
        self._id = IDGenerator.generate_id()
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f'Книга(ID: {self._id}, Назва: "{self.title}", Автор: {self.author}, В наявності: {self.is_available})'

    
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def is_available(self):
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        self._is_available = is_available



class Reader:
    def __init__(self, name):
        self._id = IDGenerator.generate_id()
        self.name = name
        self._library_card = LibraryCard(self)

    def __str__(self):
        return f"Читач(ID: {self._id}, Ім`я: {self.name})"

    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def library_card(self):
        return self._library_card


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        self.books.append(book)

    def add_reader(self, reader):
        self.readers.append(reader)

    def issue_book(self, reader_id, book_id):
        book = next((book for book in self.books if book.id == book_id), None)
        reader = next((reader for reader in self.readers if reader.id == reader_id), None)

        if book and reader and book.is_available:
            book.is_available = False
            due_date = datetime.date.today() + datetime.timedelta(days=14)
            reader.library_card.add_record(book, due_date)
            print(f'Книга  "{book.title}" видана {reader.name}. Поверніть до {due_date}.')
        else:
            print(f'Неможливо видати книгу. Або книга недоступна, або рідер/книгу не знайдено.')


class LibraryCard:
    def __init__(self, reader):
        self.reader = reader
        self.records = []

    def add_record(self, book, due_date):
        self.records.append((book, due_date))

    def __str__(self):
        records_str = "\n".join([f'Книга: "{record[0].title}", Термін виконання: {record[1]}' for record in self.records])
        return f'Бібліотечна картка(Читач: {self.reader.name})\nЗаписи:\n{records_str}'



library = Library()


book1 = Book('1984', 'Джордж Орвелл')
book2 = Book('Вбити пересмішника', 'Гарпер Лі')
book3 = Book('Портрет Доріана Грея', 'Оскар Уайльд')
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


reader = Reader('Джон Доу')
library.add_reader(reader)


library.issue_book(reader.id, book1.id)


print(reader.library_card)
