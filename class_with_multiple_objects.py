class sample():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def read(self):
        print(self.name)
        print(self.age)
s1=sample("kprit",20)
s1.read()
s2=sample("abc",21)
s2.read()