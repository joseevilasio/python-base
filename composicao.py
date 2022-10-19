#!usr/bin/env python3
"""Imprime apenas os nomes iniciados com a letra B"""

names = [
    "Bruno",
    "Joao",
    "Bernardo",
    "Barbara",
    "Brian",
]

print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")
