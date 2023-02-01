import random

def play():
    user = input("what is your choice ? 'r' for rock,'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'You won!'
    return 'You lost!'

def is_win(player,opponent):
    # return true if player wins
    if (player =='r' and opponent =='s') or(player == 's' and opponent =='p') or (player == 'p' and opponent =='r'):
        #return true
        return True

print(play())