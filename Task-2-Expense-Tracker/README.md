# Task 2 — Expense Tracker

A simple command-line Expense Tracker built using Python. The program allows users to enter multiple expenses and calculates the total amount spent.

## Author

**Muhammad Hussain**  
**Email:** hussainazeezz@outlook.com

## Features

- Enter multiple expenses
- Calculate the total amount spent
- Count the number of transactions
- Display a running total
- Type `quit` to stop entering expenses
- Handles invalid input
- Prevents negative expenses

## Concepts Used

- Functions
- `while` loop
- `if` statements
- Variables
- Arithmetic operators
- `try-except`
- String methods
- User input

## How It Works

1. The program starts the Expense Tracker.
2. The user enters an expense amount.
3. The expense is added to the total.
4. The transaction counter increases.
5. The running total is displayed.
6. The user can continue entering expenses.
7. Typing `quit` ends the program.
8. A final summary displays the number of transactions and total amount spent.

## How to Run

Make sure Python 3 is installed on your computer.

Run the following command:

```bash
python task2_expense_tracker.py
```

## Example

```text
=== Expense Tracker ===
Enter an expense amount or type 'quit' to stop.

Enter expense (or 'quit'): 50
Added: 50
Running Total: 50

Enter expense (or 'quit'): 100
Added: 100
Running Total: 150

Enter expense (or 'quit'): quit

=== Expense Summary ===
Transactions Logged: 2
Total Spent: 150
```

## File

```text
task2_expense_tracker.py
```

## Learning Objective

The purpose of this task is to practice using loops, variables, conditional statements, arithmetic operations, user input, and exception handling in Python.
