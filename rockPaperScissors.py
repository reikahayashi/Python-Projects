#game of rock, paper, scissors against computer

import random

def play():
    user = input("Input 'rock' for rock, 'paper' for paper, 'scissors' for scissors: ")
    computer = random.choice(['rock','paper','scissors'])

    if user == computer:
        return 'It\'s a tie'

    if win(user,computer):
        return "You won!"

    else:
        return "You lost!"

def win(player, opponent):
    if (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent == "paper")
    or (player == "paper" and opponent == "rock"):
        return True



play()
