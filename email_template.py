email_template = """
Olá, {nome}
Tem interesse em comprar {produto}?
Este produto é ótimo para resolver
{texto}
Clique agora em {link}

Apenas {quantidade} disponiveis!
Preço promocional {preco:.2f}
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_template.format
        (
            nome=cliente,
            produto="caneta",
            texto="Escrever muito bem",
            link="https://caneta.com.br",
            quantidade=1,
            preco=50.5,
        )
    )
