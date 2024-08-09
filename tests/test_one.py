import pytest
from ki import Library, Books

def test_library_add_pyblication():
    lib = Library()
    book = Books(1, "Hobbit", "Tolkien", 1937)
    lib.add_publications(book)
    assert book in lib.publications.values()