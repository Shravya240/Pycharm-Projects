import json
from BankAcc import Savings_Account,Checking_Account
from BankCustomer import Bank_Customer

def save_cutomers_details_into_file(accounts):
    base_dir = os.getcwd()  # Get the Current Working Directory
    file_path = os.path.join(base_dir, 'db', 'data.json')  # Join to new folder and file on it
    # data = [acc.send_to_dict() for acc in accounts ]     # Adavance Technique Name : List Comprehension
    for acc in accounts:
        print(acc.get_balance())
    # with open(file_path, "a") as f:      # OPen that File and Save the data
    #     json.dump(data, f, indent=4)
    # print("Data saved succesfully!")

# All Transaction from here  - Main Application
customer1 = Bank_Customer("Shravya" )

savings1 = Savings_Account("ACC12343523", 0)
savings2 = Savings_Account("ACC78345683", 0)
checking = Checking_Account("ACC2342y3", 0)

# Connect Bank Customer with Bank Account
customer1.add_account(savings1)
customer1.add_account(savings2)
customer1.add_account(checking)

customer1.show_accounts()