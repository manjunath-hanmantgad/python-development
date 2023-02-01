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
#guess(10) # here x = 10

# making the computer guess the number

def computer_guess(x):
    low = 1 # specify start
    high = x # this is a number which computer should guess
    feedback = '' # nothing is too high nothing to low
    while feedback != 'c' and low != high:# a random character

        guess = random.randint(low,high)
        # ask feedbac from user
        feedback = input(f"is {guess} too high {H}, too low {L}, or correct {c}").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"computer guess correctly {guess}.")

computer_guess(10)
