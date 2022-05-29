####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


class Account:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, pay: int) -> None:
        self.balance = self.balance + pay
        print("Deposit Accepted")

    def withdraw(self, pay: int) -> None:
        actual_pay = self.balance - pay
        assert actual_pay > 0, "You cant realize this operation"
        self.balance = actual_pay
        print("Withdrawal Accepted")

    def __repr__(self) -> str:
        return f"The account owner is {self.owner} and your balance is {self.balance}"


# 1. Instantiate the class
acct1 = Account("Jose", 100)


# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
acct1.owner


# 4. Show the account balance attribute
acct1.balance


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)


acct1.withdraw(75)


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
