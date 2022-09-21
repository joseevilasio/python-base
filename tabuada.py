#! /usr/bin/env python3
"""Imprime a tabuada do 1 ao 10
Tabuada 1

1 x 1 = 1

"""
__version__ = "0.1.0"
__author__ = "Jose Junior"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = list(range(1, 11))

for number in numbers:

    print(f"Tabuada do número: {number}")
    for other_number in numbers:
        print(f"{number * other_number}")
    print("_" * 40)
