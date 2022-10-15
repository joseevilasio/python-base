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
import logging
import sys

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("jose", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

# Configuração de diretório de Arquivos
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
    "room": [],
    "client": [],
    "days": [],
}

# Reservas, carregar dados no dict reservations
try:
    for line in open(filepath_reservation):
        client, room, days = line.replace("\n", "").split(",")
        reservations["client"].append(client)
        reservations["room"].append(room)
        reservations["days"].append(room)

    # Quartos, carregar dados no dict rooms
    for line in open(filepath_room):
        codigo, room, price = line.replace("\n", "").split(",")
        rooms["codigo"].append(codigo)
        rooms["room"].append(room)
        rooms["price"].append(price)

        if room in reservations["room"]:
            print("disponivel")
except FileNotFoundError as e:
    log.error("Falha na conexão com banco de dados - %s", str(e))
    sys.exit(1)

# Exibir informações para usuário
""" for key_rooms, value_rooms, in rooms.items():
    # Exibir informações para usuário
    print(f"Quartos --> {value_rooms}") """


# Input de dados do usuário
while True:
    # input
    client = input("Digite o seu nome: ").strip().title()
    try:
        codigo = int(input("Código do quarto selecionado: "))
        days = int(input("Quantidade de dias: "))
    except ValueError as e:
        log.error("É preciso inserir um número inteiro - %s", str(e))
        sys.exit(1)
        break

    # Atribuição do Quarto relacionado ao codigo e validação de reserva
    for value_codigo, value_room in zip(rooms["codigo"][1:], rooms["room"][1:]):
        if codigo == int(value_codigo):
            room = value_room
            break

    infor_input = f"{client},{room},{days}"

    try:
        # TODO: Arquivo para dá certo tem que já ter uma linha em branco, verificar forma de resolver
        with open(filepath_reservation, "a") as file_:
            file_.write("".join(infor_input) + "\n")
    except PermissionError as e:
        log.error("Sem permissão para acessar o banco de dados - %s", str(e))
        sys.exit(1)
        break

    break

# print(reservations)
# print(rooms)

#print(f"Sr(a) {client}, resersa realizada. Quarto {codigo}, {days} dias, valor total R$ XXX")
