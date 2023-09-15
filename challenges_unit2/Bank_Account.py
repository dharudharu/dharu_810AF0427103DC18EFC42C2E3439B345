class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!!welcome to the deposit & withdawal machine")
    def deposit(self):
        amount=float(input("Enter amount to deposited:"))
        self.balance+=amount
        print("\ amount deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\ you withdraw amount:",amount)
        else:
            print("\n insufficient balance")
    def display(self):
        print("\n net available balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
    
