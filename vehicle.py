class vehicle:
    brand1="BMW"
    model1="M4"
    def display_details(self):
        print(self.brand1)
        print(self.model1)

class car(vehicle):
    brand="mercedes"
    model="g_class"
    def display_details1(self):
        print(self.brand)
        print(self.model)
    
class bike(vehicle):
    brand2="suzuki"
    model2="access125"
    def display_details2(self):
        print(self.brand2)
        print(self.model2)
    
d=vehicle()
e=car()
f=bike()

d.display_details()
e.display_details1()
f.display_details2()