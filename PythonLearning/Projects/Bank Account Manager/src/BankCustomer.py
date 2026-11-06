class Bank_Customer:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def show_accounts(self):
        print(self.name + "'s Accounts:")
        for acc in self.accounts:
            print(acc.get_balance())

    def handle_deposit(self, account_number):
        self.accounts = " " #We have to search account number in the list to get their position(or index number)
        amount = float(input("Enter the amount of money you would like to deposit: "))
        self.accounts[0].deposit(amount)

    def handle_withdraw(self, account_number):
        self.accounts = " "
        amount = float(input("Enter the amount of money you would like to withdraw: "))
        self.accounts[0].withdraw(amount)
