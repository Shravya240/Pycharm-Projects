class Bank_App:
    def __init__(self):
        self.filename = "Bank_Data.json"
        self.customer = " "#read the above file

    def main_menu(self):
        print("What would you like to do?:")
        print("1. View Balances")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Save and Exit")
        choice = int(input("Choose an option (1-4): "))

        if choice == "1":
#            self.customer.show_accounts()