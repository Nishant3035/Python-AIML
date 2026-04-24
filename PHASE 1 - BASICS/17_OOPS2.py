class Bankaccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Updated Balance = {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Final Balance = {self.balance}")

    def check_balance(self):
        print(f"Balance is {self.balance}")


Ac1 = Bankaccount(101, "Nishant", 100000)
Ac2 = Bankaccount(102, "Rahul", 50000)
Ac3 = Bankaccount(103, "Dewank", 20000)

Ac1.deposit(500)
Ac2.check_balance()
Ac3.withdraw(10000)