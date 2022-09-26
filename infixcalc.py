#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1:5
n2:4
9
"""
__version__ = "0.1.0"
__author__ = "Jose Junior"

import sys

arguments = {
    "operation": None,
    "n1": None,
    "n2": None,
}

if len(sys.argv[1:]) < 1:
    arguments["operation"] = input(
        "Insert operantion 'sum' 'sub' 'mul' 'div': ").strip()
    arguments["n1"] = int(input("Insert number: "))
    arguments["n2"] = int(input("Insert number: "))

# Operação

if arguments["operation"] == "sum":
    result = arguments["n1"] + arguments["n2"]
elif arguments["operation"] == "sub":
    result = arguments["n1"] - arguments["n2"]
elif arguments["operation"] == "mul":
    result = arguments["n1"] * arguments["n2"]
elif arguments["operation"] == "div":
    result = arguments["n1"] / arguments["n2"]

# Resultado

print(
    f"Operação: {arguments['operation']}\n "
    f"n1: {arguments['n1']}\n "
    f"n2: {arguments['n2']}\n "
    f"{result}"
)
