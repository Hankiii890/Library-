from abc import ABC, abstractmethod

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
    "Класс читатель, который имеет методы для взятия и возврата публикаций"
    def __init__(self, name: str):
        self.name = name
        self.borrowed_publications = []

    # Методы для взятия и удаления публикации
    pass


class Library:
    "Класс библиотека, который имеет методы для добавления, удаления публикаций и читателей"
    def __init__(self):
        self.publications = [] 
        self.readers = []

    # Методы для управления библиотекой 
    pass 


