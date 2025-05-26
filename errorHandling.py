# Error Handling Example: Division with User Input
while True:
    try:
        # Ask for the first number
        num1 = input("Enter the first number: ")
        num1 = float(num1)  # Try to convert to float

        # Ask for the second number
        num2 = input("Enter the second number: ")
        num2 = float(num2)  # Try to convert to float

        # Attempt division
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  # Exit the loop if everything succeeded

    except ValueError:
        print(
            "Error: Please enter valid numbers only (digits with optional decimal point)."
        )
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")
