class Kg():
    """"
      Этот класс вернет в виде результата значение в килограммах.
      Атрибуты : значение.
      """


    def __init__(self,value):
        self.value = value
    """
        Конструктор для класса Kg.
        Aтрибуты : значение.
    """


    def ton(self):
        return self.value*1000

    """
        Функция для подсчета кг в тоннах.
        Параметры : значение.
        Возращает значение в кг.
    """


    def centner(self):
       return self.value *100
    """
        Функция для подсчета кг в центнерах.
        Параметры : значение.
        Возращает значение в кг.
    """



    def pound(self):
        return self.value/2.205

    """
        Функция для подсчета кг в фунтах.
        Параметры : значение.
        Возращает значение в кг.
    """

    def pud(self):
         return self.value * 16.381
    """
        Функция для подсчета кг в пуде.
        Параметры : значение.
        Возращает значение в кг.
    """


value1 = Kg(6000)
print(float(value1.pound()))
print(float(value1.pud()))
print(float(value1.centner()))
print(float(value1.ton()))





