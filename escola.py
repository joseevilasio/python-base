#!/usr/bin/env python3
"""
Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.0"
__author__ = "Jose Junior"

sala1 = ["Erik", "Maia", "Gustavo", "Manoel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)

print(aula_ingles_sala1)
print(aula_ingles_sala2)