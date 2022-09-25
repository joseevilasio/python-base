#!/usr/bin/env python3
"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Jose Junior"

salas = {
    "sala1" : ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"],
    "sala2" : ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

for nome, atividade in atividades.items():    
    print(f"Aula de {nome}")
    print() 

    atividade_sala1 = set(salas["sala1"]).intersection(set(atividade))
    atividade_sala2 = set(salas["sala2"]).intersection(set(atividade))

    print("Sala 01: ", atividade_sala1)
    print("Sala 02: ", atividade_sala2)
    print("-" * 40)
