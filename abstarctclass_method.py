
from abc import ABC,abstractmethod
class polygon(ABC):
    def sides(self):
        pass

class tringle(polygon):
    def sides(self):
        print("I have 3 sides")

class square(polygon):
    def sides(self):
        print("I have 4 sides")

class pentagone(polygon):
    def sides(self):
        print("I have 5 sides")

t=tringle()
t.sides()

s=square()
s.sides()

p=pentagone()
p.sides()