class Fruits:
    def eat(self):
        print("we can't eat foods")

class Orange(Fruits):
    pass

class Apple(Fruits):
    def eat(self):
        print("apple is sweet")

org1 = Orange()
app1 = Apple()
org1.eat()  
app1.eat()  
