class Kg():
    def __init__(self,value):
        self.value = value


    def ton(self):
        return self.value*1000


    def centner(self):
       return self.value *100


    def pound(self):
        return self.value/2.205


    def pud(self):
         return self.value * 16.381


 #   def __float__(self):
 #      return float(self.value)
 # пыталась через этот метод сделать но не работает так*?

value1 = Kg(6000)
print(float(value1.pound()))
print(float(value1.pud()))
print(float(value1.centner()))
print(float(value1.ton()))
