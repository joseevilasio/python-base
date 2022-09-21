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

from ctypes import alignment


numbers = list(range(1, 11))
template = """
--- Tabela de {number} ---
    {block:>}
#################
"""

for number in numbers:
    block = ""
    for other_number in numbers:
        operation = f"{number} x {other_number} = {(number * other_number)}\n"
        block += operation
        print(template.format(number=number, block=block))
