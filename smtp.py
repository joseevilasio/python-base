#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

# Atenção para config no terminal ~ python -m smtpd -c DebuggingServer -n localhost:8025

SERVER = "localhost"
PORT = 8025

FROM = "josejunior@server.com"
TO = ["destino@server.com"]
SUBJECT = "Meu e-mail enviado via Pytohn"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá Mundo!</b>
"""

# SMTP
message = f"""\
From: {FROM}
To: {"".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
