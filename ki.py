from abc import ABC, abstractmethod
from typing import List, Dict

class Publication(ABC):
    "Абстрактный базовый класс для всех публикаций"
    def __init__(self, id, title, author, year):
        self.id = id    # Уникальный идентификатор публикации
        self.__title = title  # Название публикации
        self.__author = author    # Имя автора публикации
        self.__year = year    # Год издания публикации
        self.aviable = True     # Статус доступности


    @abstractmethod
    def __str__(self) -> str:
        """
        Возвращаем общее предствление публикации;
        Метод будет реализован в дочерних классах (тут базовая реализация) 
        """
        return f"Публикация {self.__title} Автора {self.__author} Выпущена: {self.__year}"
    

class Books(Publication):
    def __str__(self):
        return f"Книга {self.__title} \n автор: {self.__author} \n год издания: {self.__year}"


class  Magazines(Publication):
    "Класс Журналы"
    def __str__(self):
        return f"Журнал {self.__title} \n автор: {self.__author} \n год издания: {self.__year}"


class Newspapers(Publication):
    "Класс Газеты"
    def __str__(self):
        return f"Газета {self.__title} \n автор: {self.__author} \n год издания: {self.__year}"


class Reader:
    """Класс читатель, который имеет методы для взятия и возврата публикаций,
    а так же используем аннотацию типов (typing)
    """
    def __init__(self, name: str):
        self.name = name
        self.borrowed_publications: List[Publication] # Список всех публикация, которые взял читатель


    def borrow(self, publication:Publication):
        "Функция взятия публикаций юзерами"
        if publication.aviable:
            publication.aviable = False # Указываем, что публикация больше не доступна для взятия другими пользователями 
            self.borrowed_publications.append(publication)
            return f"Пользователь {publication.name} взял публикацию {publication.__title}"
        else:
            return f"Публикация {publication.__title} уже используется!"


    def return_publication(self, publication: Publication):
        """
        Функция проверки заимствованных публикаций
        """
        if publication in self.borrowed_publications:
            publication.aviable = True 
            self.borrowed_publications.remove(publication)
            return f"Пользователь {self.name} вернул публикацию {publication.__title}"
        else:
            return f"Пользователь не брал {publication.__title}"
        
            
class Library:
    """
    Класс для хранения публикаций и читателей
    """
    def __init__(self):
        self.publications: Dict[int, Publication] = {}
        self.readers: List[Reader] = []


    def add_publications(self, publication: Publication):
        """
        Функция добавления публикаций
        """
        self.publications[publication.id()] = publication
        return f"Добавлена публикация: {publication.__title()}"

    
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
        return f"Читатель {self.reader} добавлен!" 


    def unregister_readers(self, reader: Reader):
        """
        Функция удаления читателей
        """
        if reader in self.readers:
            self.readers.remove(reader)
            return f"Читатель {reader} удалён"
        else:
            return f"Читатель не найдет"


    def lst_piblication():
        """
        Список зарегистрированных публикаций
        """
        pass 


lib = Library()

reader = Reader("Kirill")

book_1 = Books(1, "Hibbit", "Tolkien", 1937)
book_2 = Books(2, "Grokking algorithms", "Aditya Bhargava", 2017)

lib.add_publications(book_1, book_2)

