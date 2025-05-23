print("Hello am a programmer.")

count = 1
while count % 5:
    print(count)
    count += 1

# guess number game
import random


guess = random.randint(1, 10)
print("Guess a number between 1 and 10")
while True:
    try:
        user_input = int(input("Enter your guess: "))
        if user_input == guess:
            print("You guessed it right!")
            break
        elif user_input < guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Please enter a valid number.")
