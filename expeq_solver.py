#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
from math import log
# decoration
print(stylize("\n---- | Solve simple exponential equations (aˣ = b) | ----\n", fg("red")))

# user interaction
a = float(input("a = "))
b = float(input("b = "))

# main program
def solver(base, solution):
    return log(solution, base)

try:
    exponent = stylize(round(solver(a, b), 2), fg("red"))
    expeq = stylize(f"{a}ˣ = {b}", fg("red"))
    print(f"\nExponential equation to solve: {expeq}\n")
    print(f"The solution to this exponential equation is:\n=> x = {exponent}\n")
except:
    print("\nUnable to solve this exponential equation.\n")
