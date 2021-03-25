# Author: Vina Culas
# Date: 3/24/21
# File: highlow.py
# Description: This file is a highlow game against a computer

import random
import sys 

CEILING = 100
FLOOR = 1

ANS = 0
H = 1
L = 2
J = 3

WINS = 0
LOSSES = 0


print("\nVINA'S HIGHLOW GAME\n")

while 1:
    num = random.randint(FLOOR,CEILING)
    hint = random.randint(FLOOR,CEILING)

    print("A number secret between 1-100 has been chosen."
        " Your hint is %d. Respond with 'high', 'low', 'jackpot' or 'q'"
        "to quit." % (hint))

    guess = input("\nYour Guess: ")

    if (num > hint):
        ANS = H
    elif (num < hint):
        ANS = L
    elif (num == hint):
        ANS = J

    print("The Number Was %d..." % num)

    if ((guess == "high") or (guess == "High") or
        (guess == "HIGH") or (guess == "h") or (guess == "H")):

        if (ANS == H):
            print("You Won!")
            WINS += 1
        else:
            print("You Lost!")
            LOSSES += 1

    elif ((guess == "low") or (guess == "Low") or
        (guess == "LOW") or (guess == "l") or (guess == "L")):

        if (ANS == L):
            print("You Won!")
            WINS += 1
        else:
            print("You Lost!")
            LOSSES += 1

    elif ((guess == "jackpot") or (guess == "Jackpot") or
        (guess == "JACKPOT") or (guess == "j") or (guess == "J")):

        if (ANS == J):
            print("You Won!")
            WINS += 1
        else:
            print("You Lost!")
            LOSSES += 1

    elif (guess == "q"):
        sys.exit("\n\nQuitting Game...\n")

    else:
        print("That Is Not A Valid Guess!")

    print("\nWins: %d | Losses: %d\n\n" % (WINS, LOSSES))
