expenses = []

while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Expense")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expense = (name, amount)
        expenses.append(expense)

        print("Expense Added Successfully!")

    elif choice == 2:
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n----- Expense Records -----")
            for expense in expenses:
                print(expense)

    elif choice == 3:
        total = 0

        for expense in expenses:
            total += expense[1]

        print("Total Spending:", total)

    elif choice == 4:
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            highest = expenses[0]

            for expense in expenses:
                if expense[1] > highest[1]:
                    highest = expense

            print("Highest Expense:")
            print(highest[0], "-", highest[1])

    elif choice == 5:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please try again.")