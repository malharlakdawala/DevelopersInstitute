class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,deposit):
        if deposit>0:self.balance+=deposit
        print(f"monedy deposited succesffuly, balance is now {self.balance}")

    def withdraw(self,withdraw):
        if withdraw>0:self.balance-=withdraw
        print(f"money withdrawn succesffuly, balance is now {self.balance}")


class MinimumBalanceAccount(BankAccount):
    def __init__(self,minimum_balance=0):
        self.minimum_balance=minimum_balance

    def withdraw(self,withdraw):
        if withdraw>0:
            if self.balance-withdraw>self.minimum_balance:
                self.balance -= withdraw

bank1 = BankAccount(1000)
bank1.deposit(200)
bank1.withdraw(300)
