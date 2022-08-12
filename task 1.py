class Nobody(): # создаем класс NOBODY
    
    # принимающий при инициализации 1 параметр - name
    def __init__(self, name):
        
        # проверяем если параметр будет равен Nobody
        if name == 'Nobody':
              self.name =' Nobody'
              
              # Если значение отличается сохранить
              #  I'm Nobody, not <name>
        else:
              self.name = 'I m Nobody, not ' + str(name)

people = Nobody('Tom') # обьект класса
print(people.name)
