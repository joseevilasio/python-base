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
import logging

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

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )        
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit(1)
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

try:
    message = msg[current_language]
except KeyError as e:
    print(f"{str(e)}")
    print(f"Language is invalid, choose from {list(msg.keys())}")
    sys.exit(1)

print(message * int(arguments["count"]))
