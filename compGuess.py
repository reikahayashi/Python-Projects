#the computer has to guess the number that the user thinks of

import random

def comp_guess(x):
    l = 1
    h = x
    reply = ""
    while reply != 'c':
        if l != h:
            guess = random.randint(l,h)
        else:
            guess = low
            
        reply = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()
        
        if reply == 'h':
            h = guess - 1
        elif reply == 'l':
            l = guess + 1

    print(f"Good job. The computer guessed {guess} correctly ")

comp_guess(100)
