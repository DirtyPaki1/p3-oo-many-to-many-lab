class Book:
    all_books = []

    def __init__(self, title):
        self._title = title
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        # Returns a list of contracts involving this book
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        # Returns a list of authors involved in contracts with this book
        return [contract.author for contract in self.contracts()]

class Author:
    all_authors = []

    def __init__(self, name):
        self._name = name
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [book for contract in self.contracts() for book in contract.book.all_books]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise TypeError("Invalid arguments for signing a contract.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book) or not isinstance(date, str) or not isinstance(royalties, int):
            raise TypeError("Invalid arguments for creating a contract.")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
