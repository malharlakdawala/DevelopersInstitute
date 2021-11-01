class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,deposit):
        if deposit>0:self.balance+=deposit

    def withdraw(self,withdraw):
        if withdraw>0:self.balance-=withdraw

class MinimumBalanceAccount(BankAccount):
    def __init__(self,):