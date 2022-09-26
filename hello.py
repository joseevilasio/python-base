#!/usr/bin/env python3
"""Hello Wordl Multi Language

Dependendo da Lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar

Tenha a variavel LANG devidamente configurada ex

   export LANG=pt_BR

Execucao

   python3
   ou
   ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Jose Junior"
__license__ = "Unlincense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    current_language = os.getenv("LANG")
    # TODO: Usar repetição
    if current_language is None:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
}

print(msg.get(current_language, "Hello, World!") * int(arguments["count"]))
