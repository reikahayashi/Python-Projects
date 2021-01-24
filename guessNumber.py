import random

def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x} "))

        if guess < random_number:
            print("Guess is too low! Try Again")
        elif guess > random_number:
            print("Guess is too high! Try Again")

    print(f'Good job. You guessed {random_number} correctly ')
            
        
        
guess(100)


