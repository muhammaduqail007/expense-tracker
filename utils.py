from datetime import datetime
import csv

def get_amount():
    while True:
        amount = input("Enter the amount: ")
        try:
            amount = float(amount)
            if amount<=0:
                print("Please enter a positive amount: ")
            else:
                return amount
        except ValueError:
            print("Please enter a valid amount")




def add_expense(expenses):
    am = get_amount()
    cat = get_text("Enter Category: ")
    des = get_text("Enter Description: ")
    dat = get_date()
    expense = {"Amount":am,
            "Category":cat,
            "Description":des,
            "Date":dat}
    expenses.append(expense)
    write_expense(expenses)
    print("EXPENSE ADDED!!")




def view_expenses(expenses):
    if not expenses:
        print("No expenses added yet")
    else:
        print("=======Expense List=======")
        for expense in expenses:
            print(f"\nAmount: {expense['Amount']}")
            print(f"Category: {expense['Category']}")
            print(f"Description: {expense['Description']}")
            print(f"Date: {expense['Date']}")



def get_text(text):
    while True:
        value = input(text).strip()
        if value:
            return value
        else:
            print("Empty input not accepted!!!Try again")



def get_date():
    while True:
        dat = input("Enter date (yyyy-mm-dd): ").strip()
        try:
            datetime.strptime(dat, "%Y-%m-%d")
            return dat
        except ValueError:
            print("Please enter valid date according to given format!")
                


def write_expense(expenses):
    with open('expenses.csv','w',newline='') as csvf:
        headers = ['Amount','Category','Description','Date']
        wrt = csv.DictWriter(csvf,fieldnames=headers)
        wrt.writeheader()
        wrt.writerows(expenses)



def read_expense(expenses):
    try:
        with open('expenses.csv','r',newline='') as csvf:
            reader = csv.DictReader(csvf)
            for row in reader:
                row['Amount'] = float(row['Amount'])
                expenses.append(row)
    except FileNotFoundError:
        pass