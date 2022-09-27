#!/usr/bin/env python3
"""Faz envio de emails via arquivo de banco de dados e template
"""
__version__ = "0.1.2"
__author__ = "Jose Junior"

import sys
import os

# Input argv
arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]

# Input file

path = os.curdir
filepath = os.path.join(path, filename)
filetemplate = os.path.join(path, "template.txt")
clientes = []

for line in open(filepath):
    # TODO: Substituir por list comprehension
    clientes.append(line.split(","))

for name, email in clientes:
    # TODO: Substituir por envio de email
    print(f"--> Enviando para o email: {email} <--\n")
    print(
        open(filetemplate).read().format
        (
            nome=name,
            produto="caneta",
            texto="Escrever muito bem",
            link="https://caneta.com.br",
            quantidade=1,
            preco=50.5,
        )
    )
