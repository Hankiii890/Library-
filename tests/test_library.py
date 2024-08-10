from ki import Library, Books

def test_add_publications():
    """
    Функция проверки добавления публикаций в словарь
    :return: Публикация Hobbit добавлена!
    """
    lib = Library()
    book = Books(1, "Hobbit", "Tolkien", 1937)
    lib.add_publications(book)  # Добавляем книгу для проверки
    assert book in lib.publications.values()