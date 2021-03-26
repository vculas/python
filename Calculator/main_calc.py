# Author: Vina Culas
# Date: 3/25/21
# File: main_calc.py
# Description: This file is a calculator

import sys
import functions

print("VINA'S CALCULATOR\n")

eq = input("Input Your Equation:\n")
#print("%s" % eq)
parsed = eq.split()

if (parsed[0].isdigit()):
    print("Is a digit")
if (parsed[0].isalpha()):
    print("Is a letter")


