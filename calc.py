# Basic Python Script: Simple Calculator

from generated_tests.python.tictactoegame import TicTacToe

def main():

    #only changing this file
    #yeeeee
    #yaa
    #yohhh
    #yooooo
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Simple operations
    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    # Displaying results
    print(f"The sum is: {sum_result}")
    print(f"The difference is: {difference}")
    print(f"The product is: {product}")
    print(f"The quotient is: {quotient}")

