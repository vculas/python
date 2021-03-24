# Author: Vina Culas
# Date: 3/24/21
# File: rps.py
# Description: This file is a rock, paper, scissors game against a computer

import random
import sys 

ROCK = 0
PAPER = 1
SCISSORS = 2

WINS = 0
LOSSES = 0
TIES = 0

print("\nVINA'S ROCK, PAPER, SCISSORS GAME\n\n")
name = input("What Is Your Opponent's Name?: ")

while 1:
    weapon = input("\nChoose Your Weapon ('Rock', 'Paper', 'Scissors' or 'q' To Quit): ")

    comp = random.randint(0,2)

    if ((weapon == "rock") or (weapon == "Rock") or 
            (weapon == "ROCK") or (weapon == "r") or (weapon == "R")):

        if (comp == 0):
            #tie
            print("%s Chose Rock..." % name)
            print("You and %s Tied!" % name)
            TIES += 1
        elif (comp == 1):
            #comp wins
            print("%s Chose Paper..." % name)
            print("You Won!")
            LOSSES += 1
        elif (comp == 2):
            #player wins
            print("%s Chose Scissors..." % name)
            print("%s Won!" % name)
            WINS += 1

    elif ((weapon == "paper") or (weapon == "Paper") or 
            (weapon == "PAPER") or (weapon == "p") or (weapon == "P")):

        if (comp == 0):
            #player wins
            print("%s Chose Rock..." % name)
            print("You Won!")
            WINS += 1      
        elif (comp == 1):
            #tie
            print("%s Chose Paper..." % name)
            print("You and %s Tied!" % name)
            TIES += 1
        elif (comp == 2):
            #comp wins
            print("%s Chose Scissors..." % name)
            print("%s Won!" % name)
            LOSSES += 1

    elif ((weapon == "scissors") or (weapon == "Scissors") or 
            (weapon == "SCISSORS") or (weapon == "s") or (weapon == "S")):

        if (comp == 0):
            #comp wins
            print("%s Chose Rock..." % name)
            print("%s Won!" % name)
            LOSSES += 1
        elif (comp == 1):
            #player wins
            print("%s Chose Paper..." % name)
            print("You Won!")
            WINS += 1
        elif (comp == 2):
            #tie
            print("%s Chose Scissors..." % name)
            print("You and %s Tied!" % name)
            TIES += 1
        
    elif (weapon == "q"):
        sys.exit("\n\nQuitting Game...\n")

    else:

        print("That Is Not A Valid Weapon!")

    print("\nWins: %d | Losses: %d | Ties: %d" % (WINS, LOSSES, TIES))

        