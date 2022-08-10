from typing import Any
class MyString():
    def __init__(self, value:Any):
        self.value = str(value)

    def __eq__(self, other):
        return
        len(self.value) == len(other.value)
        
    def __lt__(self, other):
        return len( self.value) < len(other.value)

    def __le__(self, other):
        return len(self.value ) <= len(other.value)

    def __gt__(self, other):
        return len(self.value) > len(other.value)

    def __ge__(self, other):
        return len(self.value) >= len(other.value)

value = MyString('hello')
value2 = MyString('hi')

x = value == value2
y = value > value2
z = value < value2
b = value >= value2
c = value <= value2

print(x,y,z,b,c)
