"""
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso
será exibida uma mensagem de alerta dependendo das condições:
temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
"ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."
ex:
python3 temp.py 
temperatura: 30
umidade: 90
... 
'ALERTA!!! 🥵 Perigo calor extremo'
"""
import os
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

# TODO: Mover para modúlo de utilidades


def read_inputs():
    """Inputs of user for main."""
    try:
        temperature = float(input("Insert the temperature: "))
        humidity = float(input("Insert the humidity: "))
    except ValueError as e:
        log.error("Insert number float or integer - %s", str(e))
    return temperature, humidity


while True:

    temperature, humidity = read_inputs()

    if temperature > 45.0:
        msg = "ALERTA!!! 🥵 Perigo calor extremo"
    elif temperature > 30.0 and (temperature * 3) >= humidity:
        msg = "ALERTA!!! 🥵♒ Perigo de calor úmido"
    elif 10 <= temperature and temperature <= 30:
        msg = "😀 Normal"
    elif 0 <= temperature and temperature < 10:
        msg = "🥶 Frio"
    elif temperature < 0:
        msg = "ALERTA!!! ⛄ Frio Extremo."

    print(
        f"temperature: {temperature}\n"
        f"humidity: {humidity}\n"
        f"{msg}"
    )
    if input("Press Enter for continue or any key for stop!"):
        break
