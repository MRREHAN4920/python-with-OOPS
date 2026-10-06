class Sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Intro(self):
        print(self.name)
        print(self.age)
s1=Sample("rehan",53)
s1.Intro()