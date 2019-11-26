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
joy = User("Joy Li", "joy@gmail.com")

emily.make_deposit(2800)
emily.make_deposit(100)
emily.make_deposit(100)
emily.make_withdrawal(100)
emily.make_withdrawal(20)


nicole.make_deposit(200)
nicole.make_deposit(800)
nicole.make_withdrawal(20)
nicole.make_withdrawal(10)

joy.make_deposit(10000)
joy.make_withdrawal(10)
joy.make_withdrawal(70)

emily.display_user_balance()
nicole.display_user_balance()
joy.display_user_balance()

emily.transfer_money(joy, 888)

emily.display_user_balance()

joy.display_user_balance()
