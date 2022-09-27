#!/usr/bin/env python
"""
Bloco de Notas

$ bloco_de_notas.py new "Minha Nota"
tag: tecnologia
text:

Após enter arquivo é salvo o arquivo renomeado com título escolhido minha_nota-tecnologia.txt

$ bloco_de_notas.py read --tag=tecnologia
...
"""

__version__ = "0.1.0"
__author__ = "Jose Junior"

import sys

arguments = {
    "command": None,
    "title": None,
    "tag": None,
    "text": None,
}

commands = ["new", "read"]

# Input de Dados

if not sys.argv[1:]:
    print(f"É necessário utilizar comandos para iniciar {commands}")
    sys.exit(1)

elif len(sys.argv[1:]) != 2:
    print("A quantidade de parametros é invalida -> ex: new 'nova nota' <-")
    sys.exit(1)

elif len(sys.argv[1:]) == 2:
    arguments["command"] = sys.argv[1:][0]
    arguments["title"] = sys.argv[1:][1]
    arguments["tag"] = input("tag: ")
    arguments["text"] = input("text: ")

# Validação de Dados

for key, value in arguments.items():
    print(key, value)
