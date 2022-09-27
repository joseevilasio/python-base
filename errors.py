#!/usr/bin/env python
import os
import sys

# LBYL - Look Before You Leap

if os.path.exists(("names.txt")):
    print("o arquivo existe")
    input("...")  # Race Condition
    names = open("nomes.txt").readlines()
else:
    print("[Error] File names.txt not found!")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
