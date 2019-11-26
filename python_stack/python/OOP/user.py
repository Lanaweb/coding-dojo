class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -=amount
    
    def display_user_balance(self):
        print("User:", '{},'.format(self.name), 'Balance: ${}'.format(self.account_balance))
        
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


emily = User("Emily Ding", "emily@gmail.com")
nicole = User("Nicole Ding", "nicole@gmail.com")
print(emily.name)
print(emily.email)
print(nicole.account_balance)

emily.make_deposit(200)

emily.display_user_balance()
emily.transfer_money(nicole,100)
emily.display_user_balance()
print(nicole.account_balance)
