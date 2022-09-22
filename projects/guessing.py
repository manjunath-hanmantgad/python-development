import random


def guess(x):
    random_number = random.randint(1, x)  # returns a random number for us to guess
    # we need to guess the number here
    # so loop here to get the correct number
    guess = 0 # bcoz we dont want the guess to be accidently equal to random number

    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess < random_number:
            print('Guess higher')
        elif guess > random_number:
            print("Guess lower")
        #print(guess)
    print(f"that is a good guess! and the guessed number is {random_number}")
guess(10) # here x = 10



