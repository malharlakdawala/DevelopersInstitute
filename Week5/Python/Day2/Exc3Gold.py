class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, deposit):
        if self.authenticated== True and deposit > 0:
            self.balance += deposit
            print(f"monedy deposited succesffuly, balance is now {self.balance}")
        else: print("User not authenticated or deposit negative ")

    def withdraw(self, withdraw):
        if self.authenticated== True and withdraw > 0:
            self.balance -= withdraw
            print(f"money withdrawn succesffuly, balance is now {self.balance}")

    def authenticate(self, usernamechk, passwordchk):
        if self.username == usernamechk and self.password == passwordchk:
            self.authenticated = True
            print("User Authenticated")


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, minimum_balance):
        super().__init__(balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, withdraw):
        if withdraw > 0:
            if self.balance - withdraw > self.minimum_balance:
                self.balance -= withdraw
                print(f"money withdrawn succesffuly, balance is now {self.balance}")
            else:
                print(
                    f"withdraw unsuccesful, as minimum balance needs to be maintained, balance right now is {self.balance}")


bank1 = BankAccount(1000,"tony","stark")
bank1.authenticate("tony1","stark")
bank1.deposit(200)
bank1.authenticate("tony1","stark1")
bank1.withdraw(300)

# bank2 = MinimumBalanceAccount(1000, 200)
# bank2.withdraw(300)
# bank2.withdraw(600)
