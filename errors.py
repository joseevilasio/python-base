#!/usr/bin/env python
import sys

# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil pedir perdão do que permissão)

try:
    names = open("nomes.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try:
    print(names[2])
except ValueError:
    print("[Error] Missing name in the list")
    sys.exit(1)
