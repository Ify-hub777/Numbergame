import random

random_number = random.randint(1,20)

print("Hello this is the number guessing game")

guess = int(input("Guess the number between 1-20: "))
guesses = 0

while guess > random_number:
    print("")
    print("Too high")
    guesses += 1
    guess = int(input("Try again: "))

while guess < random_number:
    print("")
    print("Too low")
    guesses += 1
    guess = int(input("Try again: "))

print("Correct")
print(f"It took you {guesses} guesses")
