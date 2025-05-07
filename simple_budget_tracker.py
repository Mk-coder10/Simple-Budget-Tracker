expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount (SAR): "))
    expenses.append((name, amount))
    print("Expense added!")

def view_expenses():
    print("\nYour Expenses:")
    for name, amount in expenses:
        print(f"{name}: {amount:.2f} SAR")
    total = sum(amount for _, amount in expenses)
    print(f"Total: {total:.2f} SAR\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
