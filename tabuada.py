#! /usr/bin/env python
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---
    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
##################
...
"""
__version__ = "0.1.1"
__author__ = "Jose Junior"

numbers = range(1, 11)

for number in numbers:
    print("{:-^18}".format(f"Tabela do {number}"))
    print()
    for other_number in numbers:
        result = number * other_number
        print("{:^18}".format(f"{number} x {other_number} = {result}"))
    print("{:#^18}".format(""))
