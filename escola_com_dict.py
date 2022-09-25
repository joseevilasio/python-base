#!/usr/bin/env python3
"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Jose Junior"

sala1 = ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = {
    "Inglês": aula_ingles,
    "Música": aula_musica,
    "Dança": aula_danca,
}

for nome, atividade in atividades.items():    
    print(f"Aula de {nome}")
    print() 

    atividade_sala1 = set(sala1).intersection(set(atividade))
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print("Sala 01: ", atividade_sala1)
    print("Sala 02: ", atividade_sala2)
    print("-" * 40)
