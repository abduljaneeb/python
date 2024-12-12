#from math import pi 
class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        #ivde self venda  math kodkumbo
        print("Area of circle : ",self.pi*self.radius*self.radius)

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        print("Area of rectangle ",self.length*self.width)

def area(shape):
    shape.calculate_area()

r=int(input("enter radius :" ))
cir=circle(r)
l=int(input("enter length of ractangle : "))
b=int(input("enter breadth of rectangl : "))
rect=rectangle(l,b)
area(cir)
area(rect)
        
