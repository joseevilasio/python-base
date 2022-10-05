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

while True:

    try:
        temperature = float(input("Insert the temperature: "))
        humidity = float(input("Insert the humidity: "))
    except ValueError as e:
        print(f"{str(e)}")
        print("Insert number float or integer")
        continue

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
