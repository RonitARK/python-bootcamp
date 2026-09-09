
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"{self.owner}'s balance is: {self.balance}")


account = BankAccount("Ronit", 1000)

account.deposit(500)
account.withdraw(200)

account.show_balance()