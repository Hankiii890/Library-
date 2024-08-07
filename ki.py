from abc import ABC, abstractmethod
from typing import List, Dict

class Publication(ABC):
    "Абстрактный базовый класс для всех публикаций"
    def __init__(self, id, title, author, year):
        self.id = id    # Уникальный идентификатор публикации
        self._title = title  # Название публикации
        self._author = author    # Имя автора публикации
        self._year = year    # Год издания публикации
        self.available = True     # Статус доступности

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year


    @abstractmethod
    def __str__(self) -> str:
        """
        Возвращаем общее представление публикации;
        Метод будет реализован в дочерних классах (тут базовая реализация) 
        """
        return f"Публикация {self.title} Автора {self.author} Выпущена: {self.year}"
    

class Books(Publication):
    def __str__(self):
        return f"Книга {self.title} \n автор: {self.author} \n год издания: {self.year}"


class  Magazines(Publication):
    "Класс Журналы"
    def __str__(self):
        return f"Журнал {self.title} \n автор: {self.author} \n год издания: {self.year}"


class Newspapers(Publication):
    "Класс Газеты"
    def __str__(self):
        return f"Газета {self.title} \n автор: {self.author} \n год издания: {self.year}"


class Reader:
    """Класс читатель, который имеет методы для взятия и возврата публикаций,
    а так же используем аннотацию типов (typing)
    """
    def __init__(self, name: str):
        self.name = name
        self.borrowed_publications: List[Publication] = [] # Список всех публикация, которые взял читатель


    def borrow(self, *publications:Publication):
        "Функция взятия публикаций юзерами"
        for publication in publications:
            if publication.available and publication not in self.borrowed_publications:
                publication.available = False # Указываем, что публикация больше не доступна для взятия другими пользователями
                self.borrowed_publications.append(publication)
                return f"Пользователь {self.name} взял публикацию {publication.title}"
            else:
                return f"Публикация {publication.title} уже используется!"


    def return_publication(self, publication: Publication):
        """
        Функция проверки заимствованных публикаций
        """
        if publication in self.borrowed_publications:
            publication.available = True
            self.borrowed_publications.remove(publication)
            return f"Пользователь {self.name} вернул публикацию {publication.title}"
        else:
            return f"Пользователь не брал {publication.title}"
        
            
class Library:
    """
    Класс для хранения публикаций и читателей
    """
    def __init__(self):
        self.publications: Dict[int, Publication] = {}
        self.readers: List[Reader] = []


    def add_publications(self, *publications: Publication):
        """
        Функция добавления публикаций
        """
        for publication in publications:
            self.publications[publication.id] = publication
            print(f'Публикация {publication.title} добавлена!')

    
    def remove_publications(self, publication_id: int):
        """
        Функция удаления публикаций
        """
        if publication_id in self.publications:
            del self.publications[publication_id]
            return f"Публикация с таким-то {publication_id} удалена!"
        else:
            return f"Публикация с {publication_id} не найдена!"
        
    
    def register_readers(self, reader: Reader):
        """
        Функция регистрации читателей
        """
        self.readers.append(reader)
        return f"Читатель {reader} добавлен!"


    def unregister_readers(self, reader: Reader):
        """
        Функция удаления читателей
        """
        if reader in self.readers:
            self.readers.remove(reader)
            return f"Читатель {reader} удалён"
        else:
            return f"Читатель {reader} не найдет"


    def check_publication_availability(self, publication_id: int) -> bool:
        """
        Функция доступности публикации по её идентификатору 
        """
        publication = self.publications.get(publication_id)
        if publication:     # Если публикация найдена... Выводит статус доступности
            return publication.available
        else:
            return False 
        

    def lst_publications(self):
        publication_lst = []
        for publication in self.publications.values():
            publication_lst.append(str(publication))
        return "\n".join(publication_lst)

lib = Library()

reader = Reader("Kirill")

book_1 = Books(1, "Hobbit", "Tolkien", 1937)
book_2 = Books(2, "Grokking algorithms", "Aditya Bhargava", 2017)

lib.add_publications(book_1, book_2)

print(reader.borrow(book_1, book_2))







