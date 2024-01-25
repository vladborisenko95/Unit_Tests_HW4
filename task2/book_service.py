from copy import deepcopy


class Book:
    id_book: int
    title: str
    author: str


class BookRepository:
    def __init__(self, books: list[Book] = None):
        self._books = books
        if books is None:
            self._books = []

    def find_by_id(self, book_id: int) -> Book:
        return [*filter(lambda x: x.id == book_id, self._books)][0] # фильтр выступает в роли итератора и нам доступна функция next, поиск по id из списка

    def find_all(self) -> list[Book]:
        return deepcopy(self._books) # Метод deepcopy рекурсивно создает копию каждого элемента объекта и не копирует ссылки.


class BookService:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    @property
    def book_repository(self):
        return self._book_repository

    def find_by_id(self, book_id: int) -> Book:
        return self._book_repository.find_by_id(book_id)

    def find_all(self) -> list[Book]:
        return self._book_repository.find_all()