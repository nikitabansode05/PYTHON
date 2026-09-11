class Account:
    def __init__(self,balance):
        self.balance=balance
    
    def __str__(self):
        return f"The balance of this accoint is : {self.balance}"
    
    def withdraw(self, amount):
        self.balance-=amount
        
    def deposit(self,amount):
        self.balance+=amount

account1=Account(10000)
account2=Account(20000)

print(account1)
print(account2)

account1.withdraw(500)

print(account1)
print(account2)