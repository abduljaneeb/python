class car:
    company=0
    price=0
    color=0
    def car_details(self):
        print("company : ",self.company)
        print("price : ",self.price)
        print("color : ",self.color)

car1=car()
car1.company="TESLA"
car1.price=200000
car1.color="black"

car2=car()
car2.company="KIA"
car2.price=400000
car2.color="red"

car3=car()
car3.company="TATA"
car3.price=500000
car3.color="blue"

car1.car_details()
car2.car_details()
car3.car_details()
    
