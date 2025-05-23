# Example ATM withdrawal program
# ATM withdrawal program
account_balance = 1000  # Initial account balance
withdrawal_limit = 500  # Daily withdrawal limit
withdrawn_today = 0  # Amount withdrawn today
while True:
    try:
        withdrawal_amount = float(input("Enter amount to withdraw: "))
        if withdrawal_amount <= 0:
            print("Withdrawal amount must be positive.")
            continue
        if withdrawal_amount > withdrawal_limit:
            print(
                f"Withdrawal limit is {withdrawal_limit}. Please enter a smaller amount."
            )
            continue
        if withdrawal_amount > account_balance:
            print(f"Insufficient funds. Your balance is {account_balance}.")
            continue
        if withdrawn_today + withdrawal_amount > withdrawal_limit:
            print(
                f"You have already withdrawn {withdrawn_today} today. Daily limit is {withdrawal_limit}."
            )
            continue
        # Process the withdrawal
        account_balance -= withdrawal_amount
        withdrawn_today += withdrawal_amount
        print(f"Withdrawal successful! New balance: {account_balance}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ask if the user wants to continue or exit
        cont = (
            input("Do you want to make another transaction? (yes/no): ").strip().lower()
        )
        if cont != "yes":
            print("Thank you for using the ATM. Goodbye!")
            break
