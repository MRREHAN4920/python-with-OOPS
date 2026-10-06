'''create a class bank account

account holder name
acc no
balance

create methods:

deposit()
withdraw()
display_balance()


make sure withdrawl is not allowed when the balance is insufficeint

'''


class bank_account:
    acc_holder_name="abc"
    acc_no=101
    balance=23000
    
    def deposit(self):
        money=int(input("enter money : "))
        money=money+self.balance
        print(money)
        
    def withdraw(self):
        cash=int(input("cash : "))
        print(cash)
        
    def check_balance(self):
        print(self.balance)
        
a=bank_account()
print("acc_holder_name : ",a.acc_holder_name)
print("acc_no : ",a.acc_no)
print("balance : ",a.balance)

a.check_balance()
a.deposit()
a.withdraw()