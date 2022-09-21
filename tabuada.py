#! /usr/bin/env python
"""Imprime a tabuada do 1 ao 10
Tabuada 1

1 x 1 = 1

"""
__version__ = "0.1.0"
__author__ = "Jose Junior"

numbers = list(range(1, 11))

for number in numbers:

    print(f"Tabuada do número: {number}\n")
    for other_number in numbers:
        print(
            f"Número {number} vezes {other_number} = {number * other_number}")
    print("_" * 40)
