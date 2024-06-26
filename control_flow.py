#!/usr/bin/env python3

# control_flow.py

def demonstrate_control_flow():
    # If-Else Statement
    x = 10
    if x > 5:
        result_if_else = "x is greater than 5"
    else:
        result_if_else = "x is 5 or less"
    print(f"If-Else Statement: {result_if_else}")

    # For Loop
    sum_for_loop = 0
    for i in range(1, 6):
        sum_for_loop += i
    print(f"For Loop: Sum of numbers from 1 to 5 is {sum_for_loop}")

    # While Loop
    sum_while_loop = 0
    n = 1
    while n <= 5:
        sum_while_loop += n
        n += 1
    print(f"While Loop: Sum of numbers from 1 to 5 is {sum_while_loop}")

    # Try-Except Block
    try:
        division_result = 10 / 0
    except ZeroDivisionError:
        division_result = "Cannot divide by zero"
    print(f"Try-Except Block: {division_result}")

if __name__ == "__main__":
    demonstrate_control_flow()
