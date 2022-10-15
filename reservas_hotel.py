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
# Input de dados do usuário
while True:
    # Reservas, carregar dados no dict reservations
    try:
        for line in open(filepath_reservation):
            client, room, days = line.replace("\n", "").split(",")
            reservations["client"].append(client)
            reservations["room"].append(room)
            reservations["days"].append(room)

        # Quartos, carregar dados no dict rooms e exibir informações
        for line in open(filepath_room):
            codigo, room, price = line.replace("\n", "").split(",")
            rooms["codigo"].append(codigo)
            rooms["room"].append(room)
            rooms["price"].append(price)
            print(line)

    except FileNotFoundError as e:
        log.error("Falha na conexão com banco de dados - %s", str(e))
        sys.exit(1)
    # input
    client = input("Digite o seu nome: ").strip().title()
    try:
        codigo = int(input("Código do quarto selecionado: "))
        days = int(input("Quantidade de dias: "))
    except ValueError as e:
        log.error("É preciso inserir um número inteiro - %s", str(e))
        sys.exit(1)
        break

    if str(codigo) in rooms["codigo"][1:]:
        # Atribuição do Quarto relacionado ao codigo e validação de reserva
        for value_codigo, value_room, value_price in zip(rooms["codigo"][1:],
                                                         rooms["room"][1:],
                                                         rooms["price"][1:]
                                                         ):
            if codigo == int(value_codigo):
                if value_room in reservations["room"][1:]:
                    print(f"{value_room} já reservado!")
                    break

                infor_input = f"{client},{value_room},{days}"
                price_total = days * int(value_price)

                try:
                    # TODO: Arquivo para dá certo tem que já ter uma linha em
                    #  branco, verificar forma de resolver
                    with open(filepath_reservation, "a") as file_:
                        file_.write("".join(infor_input) + "\n")
                        file_.close()
                except PermissionError as e:
                    log.error(
                        "Sem permissão para acessar o banco de dados - %s",
                        str(e)
                    )
                    sys.exit(1)
                    break
                print(
                    f"Sr(a) {client}, resersa realizada com sucesso! "
                    f"{codigo}-{value_room}, {days} dias,"
                    f"valor total R$ {price_total}.")
    else:
        print(f"Quarto > {codigo} < selecionado não encontrado")
        sys.exit(1)
        break

    if input("Pressione ENTER fazer uma nova reserva ou qualquer tecla para sair "):
        break
