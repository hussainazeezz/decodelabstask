# ==========================================
# Task 2: Expense Tracker
# Name: Muhammad Hussain
# Email: hussainazeezz@outlook.com
# ==========================================

def main():
    total_expense = 0
    transaction_count = 0

    print("=== Expense Tracker ===")
    print("Enter an expense amount or type 'quit' to stop.\n")

    while True:
        user_input = input("Enter expense (or 'quit'): ").strip()

        if user_input.lower() == "quit":
            break

        try:
            expense = int(user_input)
            if expense < 0:
                print("Expense cannot be negative.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            continue

        total_expense += expense
        transaction_count += 1

        print(f"Added: {expense}")
        print(f"Running Total: {total_expense}\n")

    print("\n=== Expense Summary ===")
    print(f"Transactions Logged: {transaction_count}")
    print(f"Total Spent: {total_expense}")


if __name__ == "__main__":
    main()
