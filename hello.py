#! /usr/bin/env python3
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
__version__ = "0.1.2"
__author__ = "Jose Junior"
__license__ = "Unlincense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
		"en_US": "Hello, World!",
		"pt_BR": "Ola, Mundo!",
		"it_IT": "Ciao, Mondo!",
		"es_SP": "Hola, Mundo!",
		"fr_FR":"Bonjour Monde",
}

print(msg.get(current_language,"Hello, World!"))
