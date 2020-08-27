import sys
class Customer:
    bankname='durgasoft'

    def __init__(self,a,balance=0):
        self.name=a
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print('after deposit the balance :',self.balance)

    def withdrawl(self,amt):
        if amt>self.balance:
            print('insufficient balance :',)
            sys.exit()
        else:
            self.balance=self.balance-amt
            print("after withdrawl :",self.balance)

print('welcome to ',Customer.bankname)
name=input('enter ur name :')
c=Customer(name)
while True:
    print('d-deposit\nw-withdrawl\ne-exit')
    option=input('choose ur option :')
    if option=='d' or option=='D':
        amt=float(input('enter ur deposit :'))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('enter amount to withdrawl :'))
        c.withdrawl(amt)
    elif option=='e' or option=='E':
        print('thanks for banking')
        sys.exit()
    else:
        print('choose valid option')