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
__version__ = "0.0.1"
__author__ = "Jose Junior"
__license__ = "Unlincense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
   msg = "Ola, Mundo!"
elif current_language == "it_IT":
   msg = "Ciao, Mondo!"
elif current_language == "es_SP":   
   msg = "Hola, Mundo!"
elif current_language == "fr_FR":
   msg = "Bonjour Monde"
         
print(msg)
