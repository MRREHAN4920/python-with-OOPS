class student:
    name="abc"
    roll_no=101
    maths=40
    physics=40
    chemistry=40
    total=0
    
    def total_marks(self):
        self.total=self.maths+self.physics+self.chemistry
        print(self.total)
        
    def average(self):
        avg=(self.maths+self.physics+self.chemistry)/3
        print("average : ",round(avg, 2))
        
    def grade(self):
        if self.total>90:
            print("grade : A")
        elif self.total>=75:
            print("grade : B")
        elif self.total>=60:
            print("grade : C")
        elif self.total>=40:
            print("grade : D")
        else:
            print("fail")
            
a=student()
a.total_marks()
a.average()
a.grade()    