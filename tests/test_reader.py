from ki import Reader, Books

def test_borrow():
    """
    Функция проверки взятых публикаций

    :return: None
    """
    reader = Reader("Kirill")
    book = Books(1, "Hobbit", "Tolkien", 1937)
    reader.borrow(book)
    assert book in reader.borrowed_publications