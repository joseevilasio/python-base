email_template = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para resolver
%(texto)s
Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!
Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_template 
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://caneta.com.br",
            "quantidade": 1,
            "preco": 50.5,
        }
    )