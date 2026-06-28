class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def to_deposit(self,money):
        self.balance += money
        print(f"Deposited {money}, New balance = {self.balance}")
    def to_withdraw(self,money):
        self.balance -= money
        print(f"Withdrawing {money} new balance is {self.balance}")
    def check_balance(self):
        print(f"Balance is {self.balance}")

acc = BankAccount("001", "Nishant", 1000)
acc.to_deposit(500)
acc.to_withdraw(200)
acc.check_balance()