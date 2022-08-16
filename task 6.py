from dataclasses  import dataclass

@dataclass(order = True,frozen = True)
class Person():
    name:str
    surname:str
    age:int
    """"
      Этот класс для сравнения студентов.
      Атрибуты : имя,фамилия,возвраст.
    """


liza = Person(name='liza', surname='kohanchik', age=20)
alisa = Person(name='alisa', surname='kohanchik', age=18)

x = alisa.age < liza.age
y = alisa.surname == liza.surname
z = alisa.name > liza.name
print(x,y,z)
