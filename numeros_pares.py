#!/usr/bin/env python
"""
Faça um programa que imprime os números pares de 1 a 200

ex
'python numeros_pares.py'
'''
2
4
6
8
...
'''
"""

for n in range(1, 201):
    if n % 2 == 0:
        print(n)

n = 0
while n < 201:
    if n % 2 != 0:
        n += 1
        continue
    print(n)
    n += 1