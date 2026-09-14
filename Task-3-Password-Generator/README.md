# Task 3 — Random Password Generator

A simple command-line Random Password Generator built using Python. The program generates a random password based on the length provided by the user.

## Author

**Muhammad Hussain**  
**Email:** hussainazeezz@outlook.com

## Features

- Allows the user to choose the password length
- Generates a random password
- Uses uppercase and lowercase letters
- Uses numbers
- Validates the password length
- Handles invalid input
- Uses Python's `secrets` module for random character selection

## Concepts Used

- Functions
- `while` loop
- `for` loop
- `try-except`
- Conditional statements
- String concatenation
- Python modules
- `string` module
- `secrets` module
- User input

## How It Works

1. The program asks the user for a password length.
2. The input is checked to make sure it is a valid number.
3. The password length must be at least 1.
4. A character pool containing uppercase letters, lowercase letters, and numbers is created.
5. Random characters are selected until the requested length is reached.
6. The generated password is displayed.

## How to Run

Make sure Python 3 is installed on your computer.

Run the following command:

```bash
python task3_password_generator.py
```

## Example

```text
=== Random Password Generator ===
Enter desired password length: 12

Generated Password:
aK7pQ2mX91Ld
```

## Modules Used

### `string`

Used to provide uppercase and lowercase letters and numbers.

### `secrets`

Used to randomly select characters for the password.

## File

```text
task3_password_generator.py
```

## Learning Objective

The purpose of this task is to practice using functions, loops, exception handling, string manipulation, and Python's built-in modules to create a practical application.
