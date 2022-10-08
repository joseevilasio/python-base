#!/usr/bin/env python
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponiveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por virgulas.
'quartos.txt'
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas
'reservas.txt'
# cliente, quarto, dias
Bruno, 3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
__version__ = "0.1.0"
__author__ = "Jose Junior"

import os

path = os.curdir
filepath_room = os.path.join(path, "quartos.txt")
filepath_reservation = os.path.join(path, "reservas.txt")

room = {}
reservation = {}

for line in open(filepath_room):
    codigo, nome, preco = line.split(",")
    print(f"{codigo} - {nome} - R$ {preco}")
    