import csv
import os
from tkinter import *
from tkinter import ttk, messagebox
class ExpenseTracker:

    def __init__(self, window):
        self.window = window
        self.item_var = StringVar()
        self.amount_var = DoubleVar()
        self.category_var = StringVar()
        self.filename = "expenses.csv"
        self.setup_ui()
        self.read_file()

    def setup_ui(self):
        # --- Input Frame ---
        input_frame = LabelFrame(self.window, text="Add New Expense")
        input_frame.pack(fill="x", padx=10, pady=10)

        Label(input_frame, text="Item:").grid(row=0, column=0, padx=5)
        Entry(input_frame, textvariable=self.item_var).grid(row=0, column=1, padx=5)

        Label(input_frame, text="Amount:").grid(row=0, column=2, padx=5)
        Entry(input_frame, textvariable=self.amount_var).grid(row=0, column=3, padx=5)

        Label(input_frame, text="Category:").grid(row=1, column=0, padx=5, pady=10)
        categories = ["Food", "Transport", "Rent", "Leisure", "Other"]
        ttk.Combobox(input_frame, textvariable=self.category_var, values=categories).grid(row=1, column=1)

        Button(input_frame, text="Add Expense", command= self.add_expenses).grid(row=1, column=3, pady=10)  #Button calling the functionality add_expenses using the command argument

        # --- Table Frame ---
        table_frame = Frame(self.window)
        table_frame.pack(fill="both", expand=True, padx=10)

        columns = ("item", "amount", "category")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        self.tree.heading("item", text="Item")
        self.tree.heading("amount", text="Amount ($)")
        self.tree.heading("category", text="Category")
        self.tree.pack(fill="both", expand=True)

        # --- Footer ---
        Button(self.window, text="Delete Selected", command= self.delete_expenses).pack(pady=5)
        self.total_label = Label(self.window, text="Total Spent: $0.00", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)

    def add_expenses(self):
        item = self.item_var.get()
        amount = self.amount_var.get()
        category = self.category_var.get()

        if amount > 0 and item != "":
            self.tree.insert("", "end", values=(item, amount, category))
            self.save_to_file(item, amount, category)
            self.total_money()
        else:
            messagebox.showwarning("Input Error!", "Please provide an acceptable value.")

    def delete_expenses(self):
        selected = self.tree.selection()

        if selected:
            for item in selected:
                item_values = self.tree.item(item, 'values')
                item_text = self.tree.item(item, 'text')
                print(f"Item ID: {item}, Text: {item_text}, Values: {item_values}")
                self.tree.delete(item)
                self.update_file()
            self.total_money()
        else:
            messagebox.showwarning("Selection Error!", "Please select an expense to delete.")


    def total_money(self):
        total = 0
        for row in self.tree.get_children():
            amt = (self.tree.item(row)['values'][1])
            total = total + float(amt)
        #print(total)
        self.total_label.config(text = f"Total Spent: ${total}")

    def save_to_file(self, item, amount, category):
        file_exists = os.path.isfile(self.filename)
        with open(self.filename, mode = 'a', newline = '') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Item", "Amount", "Category"])
            writer.writerow([item, amount, category])

    def update_file(self):
        pass

    def read_file(self):
        if os.path.isfile(self.filename):
            with open(self.filename, mode = 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    self.tree.insert("", "end", values = row)
            self.total_money()



if __name__ == "__main__":
    window = Tk()
    window.title("Expense Tracker App")
    window.geometry("600x500")
    app = ExpenseTracker(window)
    window.mainloop()

