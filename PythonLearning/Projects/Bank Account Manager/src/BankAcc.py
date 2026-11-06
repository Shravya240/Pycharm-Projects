import json
class Bank_Account: #Parent class- superclass
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        # We use a leading underscore to signal this is "private"
        # (Encapsulation: don't touch __balance directly!)
        self.__balance = balance

    def send_to_dict(self):         #Converting object to dictionary
        return{
            "owner": self.owner,
            "balance": self.__balance,
            "type": self.__class__.__name__
        }


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return f"Account owner: {self.owner} | Balance: ${self.__balance}"

class Savings_Account(Bank_Account): #Chid class- derived class (inheritance)
    def __init__(self, owner, balance, interest_rate=0.02):
        super().__init__(owner=owner, balance=balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        current_bal = self._Bank_Account__balance
        interest = current_bal * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest:.2f} applied at {self.interest_rate*100}%")

class Checking_Account(Bank_Account):
    def __init__(self, owner, balance, fees= 1.0):
        super().__init__(owner=owner, balance=balance)
        self.transaction_fees = fees

    def withdraw(self, amount):
        total_deduction = amount + self.transaction_fees
        super().withdraw(total_deduction)
