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

Os resultados serão salvos em "infixcalc.log"
"""
__version__ = "0.1.3"
__author__ = "Jose Junior"

import sys
import os

# Dados

arguments = {
    "operation": None,
    "n1": None,
    "n2": None,
}

valid_operantions = ("sum", "sub", "mul", "sub")

# Input de Dados

if not sys.argv[1:]:
    arguments["operation"] = input(
        "Insert operantion 'sum' 'sub' 'mul' 'div': ").strip()
    arguments["n1"] = input("Insert number: ")
    arguments["n2"] = input("Insert number: ")

# Buscando dados da argv

elif len(sys.argv[1:]) == 3:
    arguments["operation"] = sys.argv[1:][0]
    arguments["n1"] = sys.argv[1:][1]
    arguments["n2"] = sys.argv[1:][2]

# Validação

elif len(sys.argv[1:]) != 3:
    print("Option numbers invalid")
    print("Ex: sum 5 5")
    sys.exit(1)

for key, value in arguments.items():
    if key == "operation":
        if arguments["operation"] not in valid_operantions:
            print(f"Invalid Option '{arguments['operation']}'")
            print(valid_operantions)
            sys.exit(1)
    if key in ("n1", "n2"):
        if not arguments[key].replace(".", "").isdigit():
            print(f"Option invalid {arguments[key]}")
            sys.exit(1)
        if "." in arguments[key]:
            arguments[key] = float(arguments[key])
        else:
            arguments[key] = int(arguments[key])

# Operação

if arguments["operation"] == "sum":
    result = arguments["n1"] + arguments["n2"]
elif arguments["operation"] == "sub":
    result = arguments["n1"] - arguments["n2"]
elif arguments["operation"] == "mul":
    result = arguments["n1"] * arguments["n2"]
elif arguments["operation"] == "div":
    result = arguments["n1"] / arguments["n2"]

# Criar log

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
with open(filepath, "a") as file_:
    file_.write(
        f"Operação: {arguments['operation']} n1: {arguments['n1']} n2: {arguments['n2']} -> {result}\n")

# Resultado

print(
    f"Operação: {arguments['operation']}\n "
    f"n1: {arguments['n1']}\n "
    f"n2: {arguments['n2']}\n "
    f"{result}"
)