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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()
        self.accountPlus = BankAccount(int_rate=0.03, balance =20)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        self.accountPlus.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        self.accountPlus.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User:", '{},'.format(self.name), 'Balance: ${}'.format(self.account.balance))
        print("User:", '{},'.format(self.name), 'Balance: ${}'.format(self.accountPlus.balance))
        return self
        
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        self.accountPlus.withdraw(amount)
        other_user.account.deposit(amount)
        return self


