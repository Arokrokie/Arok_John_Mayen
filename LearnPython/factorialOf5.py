# Program to calculate the factorial of 5 (five) 5!


def calculate_factorial(n):
    """Calculate the factorial of a non-negative integer"""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Calculate factorial of 5
number = 5
factorial_result = calculate_factorial(number)

# Display the result
print(f"The factorial of {number} is: {factorial_result}")
