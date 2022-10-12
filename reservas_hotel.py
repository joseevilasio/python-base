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

# Config diretório de Arquivos
path = os.curdir
filepath_room = os.path.join(path, "quartos.txt")
filepath_reservation = os.path.join(path, "reservas.txt")

# Estrutura de dados
rooms = {
    "codigo": [],
    "room": [],
    "price": [],
}

reservations = {
    "codigo": [],
    "room": [],
    "client": [],
    "status": [],
    "days": [],
}

# Reservas, inserir no dict
for line in open(filepath_reservation):
    client, room, days = line.replace("\n", "").split(",")
    reservations["client"].append(client)
    reservations["room"].append(room)
    reservations["days"].append(room)

# Quartos, inserir no dict
for line in open(filepath_room):
    codigo, room, price = line.replace("\n", "").split(",")
    rooms["codigo"].append(codigo)
    rooms["room"].append(room)
    rooms["price"].append(price)

# Inserir dados do usuário
while True:

    client = input("Digite o seu nome: ").strip().title()
    codigo = int(input("Código do quarto selecionado: "))
    days = int(input("Quantidade de dias: "))

    infor_input = f"{client},{codigo},{days}"

    # TODO: Arquivo para dá certo tem que já ter uma linha em branco, verificar forma de resolver
    with open(filepath_reservation, "a") as file_:
        file_.write("".join(infor_input) + "\n")

    break

print(reservations)
print(rooms)

print(f"Sr(a) {client}, resersa realizada. Quarto {codigo}, {days} dias, valor total R$ XXX")
