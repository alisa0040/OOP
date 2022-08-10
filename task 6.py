from dataclasses  import dataclass

@dataclass
class Person():
    name:str
    surname:str
    age:int

    def __init__(self, name, surname, age):
       self.__name = name
       self.__surname = surname
       self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname



liza = Person(name='liza', surname='kohanchik', age=20)
alisa = Person(name='alisa', surname='kohanchik', age=18)

x = alisa.age < liza.age
y = alisa.surname == liza.surname
z = alisa.name > liza.name
print(x,y,z)
