class Student(): # создаем класс  студент
    def __init__(self, first_name, last_name, group, *mark): # атрибуты first_name, last_name, group и marks.
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.mark = mark
        self.marks = []
        self.marks.append(mark)

    def __str__(self):
        return' Student(first name=%s, last name=%s,group=%s,marks=%s)' % (self.first_name,self.last_name,self.group,self.mark)

    # Метод класса
    def add_mark(self, *mark) :# Принимает оценку и добавляет в marks
        # Если значение меньше 0 или больше 10, то значение не добавляется
        if not 10 < mark[0] or mark[0] < 0:
            return self.marks.append(mark)
        else:
            return None


    # Метод класса
    def get_average_mark(self):# Возвращает средний балл
        if len(self.marks) == 0:
            return 0
        else:
            return sum(self.mark) / len(self.marks)

    # Метод класса
    # Возвращает сумму стипендии.
    def get_scholarship(self):
        # Если средняя оценка студента равна 5, то сумма 500, иначе 150
        if self.get_average_mark() == 5 :
            return 500
        else:
            return 150

class Aspirant(Student): # наследование класса студента

    def __init__(self,first_name, last_name, group,scientific_publications,*mark): # + атрибуты scientific_publications
        super().__init__(first_name, last_name, group,* mark)
        self.scientific_publications = scientific_publications

    def __str__(self):
        return ' Aspirant(first name=%s, last name=%s,group=%s,scientific_publications=%s,marks=%s)' % \
               (self.first_name, self.last_name, self.group,self.scientific_publications,self.mark)

    # переопределение метода класса
    # Возвращает сумму стипендии.
    def get_scholarship(self):
        # Если средняя оценка аспиранта равна 5, то сумма 700, иначе 250.
        if self.get_average_mark() == 5:
             return 700
        else:
             return 250


student =  Student('Andrey','BOTY','6',7,9)
print(student)

aspirant= Aspirant('Aspirante','BOTY','6','work',2,9)
print(aspirant)

aspirant.add_mark(3,9)
student.add_mark(4,8)


print(student.get_average_mark())
print(aspirant.get_average_mark())
print(student.get_scholarship())
print(aspirant.get_scholarship())
