# Import the math library to use the factorial function
import math

# Define a class called FactorialCalculator
class FactorialCalculator:
    # Define an __init__ method that takes a number as an argument and assigns it to an instance variable called self.number
    def __init__(self, number):
        self.number = number
    
    # Define a method called calculate_factorial that returns the factorial of self.number using math.factorial
    def calculate_factorial(self):
        return math.factorial(self.number)
    
    # Define a method called print_result that prints the result of calculate_factorial in a formatted string
    def print_result(self):
        print(f"The factorial of {self.number} is {self.calculate_factorial()}")

# Ask the user to enter a positive integer and store it in a variable called user_input
user_input = input("Please enter a positive integer: ")

# Try to convert user_input to an integer and store it in a variable called user_number
try:
    user_number = int(user_input)
# If user_input is not a valid integer, print an error message and exit the program
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()
# If user_number is negative, print an error message and exit the program
if user_number < 0:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Create an instance of FactorialCalculator with user_number as an argument and store it in a variable called calculator
calculator = FactorialCalculator(user_number)

# Call the print_result method of calculator
calculator.print_result()
