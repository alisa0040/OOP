class Nobody():

    # принимающий при инициализации 1 параметр - name
    def __init__(self, name):
        self.name = name

    def get_name(self):
        #проверяем если параметр будет равен Nobody
        if self.name != 'Nobody':

           # Если значение отличается сохранить
           #  I'm Nobody, not <name>
            print(f'I m Nobody, not {self.name}')
        else:
            return self.name

Tom = Nobody('Tom') # обьект класса
rik = Nobody('Nobody') # обьект класса

rik.get_name()
Tom.get_name()
