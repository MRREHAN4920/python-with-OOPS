'''employee salary

create a class employee

employee id
name
basic salary

create a method to calc the total salary

HRA = 20% of basic salary
DA = 10% of basic salary
total salary = basic + HRA + DA
'''



class employee:
    employee_id=101
    name="abc"
    basic_salary=20000
    
    def total_salary(self):
       HRA=0.2*self.basic_salary
       DA=0.1*self.basic_salary
       total=HRA+DA+self.basic_salary
       print("total salary : ",total)
        
d=employee()
print(d.employee_id)
print(d.name)
print(d.basic_salary)

d.total_salary()