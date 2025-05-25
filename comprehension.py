# List and dictionary comprehensions
# List comprehension

# square = [x**2 for x in range(10)]
# print(square)


# Example four: List comprehension with condition
numbers = [1, 2, 3, 4, 5]
square_dict = {x: x**2 for x in numbers}
print(square_dict)

# List comprehension with condition
# Must be even numbers
even_square = [x**2 for x in range(10) if x % 2 == 0]
print(even_square)

# Exercise 1: Real world example:
# Exercise  three: Create an ATM withdrawal program - use if-else statement to check account balance before allowing withdrawal

# Assignment 1: Create and inventory management - Use loops to disply or update a list of stock items
