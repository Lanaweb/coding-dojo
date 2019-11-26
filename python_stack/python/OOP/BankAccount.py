class BankAccount:
    def __init__(self, int_rate=0.02, balance =0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print ('insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self
        # your code here
    def display_account_info(self):
        print('Balance: ${}'.format(self.balance))
        # your code here
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
        # your code here

plain = BankAccount()

plus = BankAccount(0.06, 20000)


plain.deposit(800).deposit(800).deposit(800).withdraw(400).yield_interest().display_account_info()

plus.deposit(1000).deposit(5000).withdraw(500).withdraw(20000).withdraw(200).withdraw(200).yield_interest().display_account_info()
