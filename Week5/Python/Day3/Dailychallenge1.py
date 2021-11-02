import math


class Circle:
    def __init__(self,radius,str):
        self.str=str
        self.radius = radius if str=="radius" else radius/2

    def circle_area(self):
        return math.pi*self.radius**2

    def __add__(self, other):
        return self.radius+other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def sort(self,other):
        d=[]
        d.append(int(self.radius))
        d.append(int(other.radius))
        d=sorted(d)
        return d


circle1 = Circle(5,"radius")
circle2= Circle(8,"diameter")

print(circle1.circle_area(),circle2.circle_area())
d=circle1+circle2
print(d)
print(circle1>circle2)

print(circle1.sort(circle2))