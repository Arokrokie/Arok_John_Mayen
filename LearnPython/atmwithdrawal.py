# Simple ATM withdrawal program
account_balance = 1000.00  # Initial account balance
daily_limit = 500.00  # Daily withdrawal limit
withdrawn_today = 0.00  # Amount withdrawn today

print("Welcome to the ATM!")
print(f"Your current balance is: ${account_balance:.2f}")
print(f"Daily withdrawal limit: ${daily_limit:.2f}\n")

while True:
    # Display available amounts
    print(f"\nAvailable to withdraw today: ${daily_limit - withdrawn_today:.2f}")
    print(f"Account balance: ${account_balance:.2f}")

    try:
        # Get withdrawal amount
        amount = float(input("\nEnter amount to withdraw (0 to exit): $"))

        # Exit condition
        if amount == 0:
            print("\nThank you for using the ATM. Goodbye!")
            break

        # Validate amount
        if amount <= 0:
            print("Amount must be positive. Please try again.")
            continue

        if amount > account_balance:
            print("Insufficient funds. Please enter a smaller amount.")
            continue

        if amount > daily_limit:
            print(f"Maximum single withdrawal is ${daily_limit:.2f}. Please try again.")
            continue

        if withdrawn_today + amount > daily_limit:
            remaining = daily_limit - withdrawn_today
            print(f"You can only withdraw ${remaining:.2f} more today.")
            continue

        # Process withdrawal
        account_balance -= amount
        withdrawn_today += amount

        print(f"\nWithdrawal successful! Dispensed ${amount:.2f}")
        print(f"New balance: ${account_balance:.2f}")
        print(f"Remaining daily limit: ${daily_limit - withdrawn_today:.2f}")

        # Ask to continue
        another = input("\nWould you like another transaction? (yes/no): ").lower()
        if another != "yes":
            print("\nThank you for using the ATM. Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
