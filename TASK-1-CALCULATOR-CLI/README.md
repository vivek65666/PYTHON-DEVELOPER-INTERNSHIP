# Python Developer Internship — Task 1

## Calculator Program

A simple command-line calculator built using **Python**. This project performs basic arithmetic operations and includes input validation and error handling.

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Handles division by zero
* Handles invalid numeric input
* Handles invalid menu choices
* Interactive command-line interface
* Beginner-friendly Python implementation

## Technologies Used

* **Python 3**
* **Command Line / PowerShell**
* **Git**
* **GitHub**

## Project Structure

```text
TASK-1/
│
├── calculator.py
└── README.md
```

## How the Program Works

When the program starts, it displays a menu with five options:

```text
===== Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
```

The user selects an operation and enters two numbers.

The program then performs the selected calculation and displays the result.

## Operations

### 1. Addition

Adds two numbers.

Example:

```text
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5
Addition result: 15
```

### 2. Subtraction

Subtracts the second number from the first number.

Example:

```text
Enter your choice (1-5): 2
Enter first number: 10
Enter second number: 5
Subtraction result: 5
```

### 3. Multiplication

Multiplies two numbers.

Example:

```text
Enter your choice (1-5): 3
Enter first number: 10
Enter second number: 5
Multiplication result: 50
```

### 4. Division

Divides the first number by the second number.

Example:

```text
Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 2
Division result: 5.0
```

The program also prevents division by zero:

```text
Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 0
Division result: Error: Cannot divide by zero.
```

### 5. Exit

Selecting option `5` exits the calculator.

```text
Enter your choice (1-5): 5
Thank you for using the calculator!
```

## Input Validation

The program handles incorrect user input.

### Invalid Menu Choice

If the user enters a number outside the range `1-5`:

```text
Enter your choice (1-5): 8
Invalid choice. Please try again.
```

### Invalid Number Input

If the user enters text instead of a number:

```text
Enter your choice (1-5): 1
Enter first number: abc
Invalid input. Please enter numbers only.
```

### Division by Zero

The program checks whether the second number is zero before performing division:

```text
Division result: Error: Cannot divide by zero.
```

## How to Run

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Open the Project Directory

```bash
cd TASK-1
```

### Step 3: Run the Program

```bash
python calculator.py
```

If your system uses `python3`, run:

```bash
python3 calculator.py
```

## Example Output

```text
===== Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice (1-5): 1
Enter first number: 20
Enter second number: 10
Addition result: 30
```

Another example:

```text
Enter your choice (1-5): 4
Enter first number: 10
Enter second number: 0
Division result: Error: Cannot divide by zero.
```

## Concepts Demonstrated

This project demonstrates fundamental Python programming concepts:

* Variables
* Data types
* User input
* Type conversion
* `if`, `elif`, and `else`
* `while` loops
* Functions
* Exception handling
* Arithmetic operators
* Input validation
* Error handling

## Learning Outcomes

Through this project, I learned how to:

1. Build an interactive Python command-line application.
2. Implement basic arithmetic operations.
3. Validate user input.
4. Handle exceptions using Python.
5. Prevent division-by-zero errors.
6. Create a menu-driven application.
7. Test different input scenarios.
8. Use Git and GitHub to manage project files.

## Testing

The calculator was tested with:

* Valid numeric inputs
* Decimal numbers
* Invalid text input
* Invalid menu choices
* Division by zero
* Multiple calculations
* Exit option

## Future Improvements

Possible improvements include:

* Add modulus operation
* Add exponentiation
* Add square root functionality
* Add calculation history
* Create a graphical user interface
* Add automated unit tests
* Improve the user interface

## Author

**Vivek C Raj**

Python Developer Intern Candidate

* GitHub: `vivek65666`
* LinkedIn: `vivekcraj`

## License

This project is created for educational and internship purposes.
