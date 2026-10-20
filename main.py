from utils import get_amount,add_expense,view_expenses,read_expense
expenses = []
read_expense(expenses)
while True:

    print("========Expense Tracker========")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()
    if choice == '1':
        add_expense(expenses)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        print("Goodbye!!!!")
        break
    else:
        print("INVALID CHOICE!!!!")

