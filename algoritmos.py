import pegar
import ir
import pedir
import tem
import comer

# Premissas
today = "Segunda"
hora_atual = 15
natal = False
chovendo = True
frio = False
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriados = ["Quarta"]
horario_padaria {
    "semana": 19,
    "fds": 12,
}

# Algoritmo

# A padaria está aberta?
if today in feriados and not natal:
    padaria_aberta = False
elif today not in semana and hora_atual < horario_padaria["fds"]:
    padaria_aberta = True
elif today in semana and hora_atual < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False

if padaria_aberta:
    if chovendo and (frio or nevando):
        pegar("guarda chuva")
        pegar("blusa")
        pegar("botas")
    elif chovendo and not frio:
        pegar("guarda chuva")
        pegar("agua")
    elif chovendo:
        pegar("guarda chuva")
    ir("padaria")

    if tem("pao integral") and tem("baguete"):
        pedir(6, "pao integral")
        pedir(6 "baguete")
    elif tem("pao integral") or tem("baguete"):
        pedir(12, "pao integral ou baguete")
    else:
        pedir(6, "qualquer pao")
else:
    comer("bolachas")
