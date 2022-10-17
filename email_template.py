#!/usr/bin/env python3
"""Faz envio de emails via arquivo de banco de dados e template
"""
__version__ = "0.1.2"
__author__ = "Jose Junior"

import sys
import os
import smtplib
from email.mime.text import MIMEText

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

with smtplib.SMTP(host="localhost", port=8025) as server:
    for line in open(filepath):
        name, email = line.split(",")
        text = (
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

        from_ = "josejunior@server.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message['Subject'] = "Compre mais"
        message['From'] = from_
        message['To'] = to

        server.sendmail(from_, to, message.as_string())
