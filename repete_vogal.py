#!/usr/bin/env python
"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

ex:

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
palavras = []

while True:

    palavra = input("Digite uma palavra (ou enter para sair): ").strip()
    palavra_final = ""

    if not palavra:
        break

    for letra in palavra:
        if letra.lower() in "aeiouâãáàêéèíìîôõóòûúù":
            palavra_final += letra * 2
        else:
            palavra_final += letra
    palavras.append(palavra_final)

print(*palavras, sep="\n")
