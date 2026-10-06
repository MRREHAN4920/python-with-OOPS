class shape:
    print("areas")
    
class circle(shape):
    def area(self):
        self.r=5
        self.area=3.14*self.r*self.r
        print("circle : ",self.area)
        
class rectangle(shape):
    def area(self):
        self.length=5
        self.breadth=2
        self.area=self.length*self.breadth
        print("rectangle : ",self.area)
        
class triangle(shape):
    def area(self):
        self.height=5
        self.base=2
        self.area=0.5*self.height*self.base
        print("triangle : ",self.area)
    
c=circle()
r=rectangle()
t=triangle()

c.area()
r.area()
t.area()