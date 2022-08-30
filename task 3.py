from typing import Any

class MyString():
    """"
      Этот класс для сравнения длин значений.
      Атрибуты : значений.
    """
    def __init__(self, value:Any):
        self.value = str(value)
    """
        Конструктор для класса MyString .
        Aтрибуты :value (любой тип данных).
    """


    def __eq__(self, other):
        return
        len(self.value) == len(other.value)
    """
        Функция сравнения == .
        Параметры : значение.
        Возращает результат сравнения .
    """

    def __lt__(self, other):
        return len( self.value) < len(other.value)
    """
        Функция сравнения < .
        Параметры : значение.
        Возращает результат сравнения .
    """
    def __le__(self, other):
        return len(self.value ) <= len(other.value)
    """
        Функция сравнения <= .
        Параметры : значение.
        Возращает результат сравнения .
    """
    def __gt__(self, other):
        return len(self.value) > len(other.value)
    """
        Функция сравнения > .
        Параметры : значение.
        Возращает результат сравнения .
    """
    def __ge__(self, other):
        return len(self.value) >= len(other.value)
    """
        Функция сравнения >= .
        Параметры : значение.
        Возращает результат сравнения .
    """
value = MyString('hello')
value2 = MyString('hi')

x = value == value2
y = value > value2
z = value < value2
b = value >= value2
c = value <= value2

print(x,y,z,b,c)
