class BankAccount:
    def __init__(self, owner, balance=0.0):
        if not owner.isalpha():
            print("error whie creatin an account")
            return
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        #if not amount.isdigit:
        #    print("argument 'parametr' must be a digit")
        #    return
        if amount <= 0:
            print("Cannot deposit a non positiv amount of money")
            return
        self.balance = self.balance + amount

    def withdraw(self, amount):
        #if not amount.isdigit:
        #    print("argument 'parametr' must be a digit")
        #    return

        if amount <= 0:
            print("Cannot widthdraw a non positiv amount of money")
            return

        if self.balance - amount< 0:
            print("Nedostatek prostředků")
            return

        self.balance = self.balance - amount

    def describe(self):
        return f"{self.owner}: {self.balance:.2f} Kč"


acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)       # Nedostatek prostředků
print(acc.describe())    # Jana: 700.00 Kč