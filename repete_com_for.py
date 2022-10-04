#!/usr/bin/env python

original = [1, 2, 3]

# For loops / Laço for
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension

dobrada = [n * 2 for n in original]
print(dobrada)