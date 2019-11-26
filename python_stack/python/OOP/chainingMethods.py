class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -=amount
        return self
    
    def display_user_balance(self):
        print("User:", '{},'.format(self.name), 'Balance: ${}'.format(self.account_balance))
        return self
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


emily = User("Emily Ding", "emily@gmail.com")
nicole = User("Nicole Ding", "nicole@gmail.com")
joy = User("Joy Li", "joy@gmail.com")

emily.make_deposit(2800).make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(20).display_user_balance().transfer_money(joy, 888).display_user_balance()



nicole.make_deposit(200).make_deposit(800).make_withdrawal(20).make_withdrawal(10).display_user_balance()

joy.make_deposit(10000).make_withdrawal(10).make_withdrawal(70).display_user_balance()


