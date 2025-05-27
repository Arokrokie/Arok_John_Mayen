# Method Overriding real life Example 1
class Vehicle:
    def make_sound(self):
        print("Vroom! (Default vehicle sound)")


class Car(Vehicle):
    def make_sound(self):  # Overrides parent's method
        print("Beep Beep! (Car horn)")


class Bike(Vehicle):
    def make_sound(self):  # Overrides parent's method
        print("Ring Ring! (Bike bell)")


# Usage
default_vehicle = Vehicle()
default_vehicle.make_sound()  # Output: "Vroom! (Default vehicle sound)"

car = Car()
car.make_sound()  # Output: "Beep Beep! (Car horn)"

bike = Bike()
bike.make_sound()  # Output: "Ring Ring! (Bike bell)"


# Real world example 2 of method overriding
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")


class SavingsAccount(BankAccount):
    def withdraw(self, amount):  # Overrides parent method
        if (
            amount <= 1000 and amount <= self.balance
        ):  # Savings account rule: Max $1000/withdrawal
            self.balance -= amount
            print(f"Withdrew ${amount} (Savings). New balance: ${self.balance}")
        else:
            print("Savings withdrawal limit exceeded or insufficient funds!")


class CheckingAccount(BankAccount):
    def withdraw(self, amount):  # Overrides parent method
        fee = 2  # Checking account has a $2 fee per withdrawal
        if amount + fee <= self.balance:
            self.balance -= amount + fee
            print(
                f"Withdrew ${amount} + ${fee} fee (Checking). New balance: ${self.balance}"
            )
        else:
            print("Insufficient funds to cover withdrawal + fee!")


# Usage
savings = SavingsAccount(5000)
savings.withdraw(800)  # Allowed: "Withdrew $800 (Savings). New balance: $4200"
savings.withdraw(1200)  # Denied: "Savings withdrawal limit exceeded..."

checking = CheckingAccount(5000)
checking.withdraw(100)  # "Withdrew $100 + $2 fee (Checking). New balance: $4898"
