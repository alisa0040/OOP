
class Student():
    """"
    Этот класс для подсчета степендии студента.
    Атрибуты : имя,фамилия,группа ,оценка.
    """
    def __init__(self, first_name, last_name, group,mark):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.mark = mark
        self.marks = []
        self.marks.append(mark)
    """"
    Конструктор для класса Student.
    Атрибуты : имя,фамилия,группа ,оценка.
    """
    def __str__(self):
        return' Student(first name=%s, last name=%s,group=%s,marks=%s)' % (self.first_name,self.last_name,self.group,self.mark)


    def add_mark(self):
        if not 10 < self.mark or self.mark  < 0:
            return self.marks.append(self.mark)
        else:
            return None
        """""
        Функция добавления оценки в список оценок.
        Параметры : оценка.
        Возращает список с добавленной оценкой.
        """

    def get_average_mark(self):
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.marks) / len(self.marks)
        """""
        Функция подсчета средней оценки.
        Параметры : список оценок.
        Возращает среднее значение оценок.
        """

    def get_scholarship(self):
        if self.get_average_mark() == 10 :
            return 500
        else:
            return 150
        """""
        Функция подсчета степендии.
        Параметры : средняя оценка.
        Возращает сумму степендии.
        """

class Aspirant(Student):
    """"
    Этот класс для подсчета степендии аспиранта.
    Атрибуты : имя,фамилия,группа ,оценка.
    """

    def __init__(self,first_name, last_name, group,scientific_publications,mark):
        super().__init__(first_name, last_name, group,mark)
        self.scientific_publications = scientific_publications
    """"
    Конструктор для класса Aspirant .
    Атрибуты : имя,фамилия,группа ,оценка ,научная работа.
    """
    def __str__(self):
        return ' Aspirant(first name=%s, last name=%s,group=%s,scientific_publications=%s,mark=%s)' % \
               (self.first_name, self.last_name, self.group,self.scientific_publications,self.mark)

    def get_scholarship(self):
        if self.get_average_mark() == 10:
             return 700
        else:
             return 250
        """""
        Функция подсчета степендии.
        Параметры : средняя оценка.
        Возращает сумму степендии.
        """

student =  Student('Andrey','BOTY','6',10)
print(student)
student.add_mark()
print(student.get_average_mark())
print(student.get_scholarship())


aspirant= Aspirant('Aspirante','BOTY','6','work',2)
print(aspirant)
aspirant.add_mark()
print(aspirant.get_average_mark())
print(aspirant.get_scholarship())
