class Person():

    """"
      Этот класс для ознакомления со студентом.
      Атрибуты : имя,фамилия,возвраст.
    """

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    """
        Конструктор для класса    Person.
        Aтрибуты : имя,фамилия,возвраст.
    """

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if (value - self.age > 1):
            print('error')
            return

        self.__age = value

    def __str__(self):
        return f'full_name = {self.name} {self.surname} '
    """
        Функция выводит строку с именем и фамилией.
        Параметры : имя ,фамилия.
        Возращает строку с именем и фамилией.
    """



liza = Person('liza', 'kohanchik', 20)
print(liza.age)

liza.age += 2
print(liza.age)

liza.age += 1
print(liza.age)

print(liza.__str__())
