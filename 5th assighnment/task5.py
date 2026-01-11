class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal.")

    def get_balance(self):
        return self.__balance

#demonstration
acc = BankAccount("Aldik")
acc.deposit(1000000)
acc.withdraw(456000)
print(acc.get_balance())