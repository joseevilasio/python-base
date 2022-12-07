"""
Este programa pergunta ao usuário quais items ele deseja comprar
e calcula o valor total da compra.

1. Clique em Run e execute o programa para ver como ele funciona.
2. Para cada um dos comentários marcados abaixo efetue as alterações
   usando orientação a objetos.
"""
from decimal import Decimal

class Produto:
    """Representa um produto"""


    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


class Compra:
    """Representa a compra"""
    items = {"items": []}

    def __init__(self, cliente):
        self.cliente = cliente
        

    def calcula_total(self, produtos):
        """Calcula o total da compra"""
        total = 0
        for cod_produto, quantidade in self.items["items"]:
            produto = produtos[cod_produto]
            total += produto.valor * quantidade
        return Decimal(total)

produtos = {
    "1": Produto(nome="Maça",valor=Decimal(4.5)),    
    "2": Produto("Melancia", Decimal(6.3)),
}

print("Olá cliente, boas vindas à quitanda!")
print("Estes são os produtos disponíveis:")
for codigo, produto in produtos.items():
    print(f"{codigo} -> {produto.nome} - R$ {produto.valor:.2f}")

compra = Compra(input("Qual o seu nome?"))


while True:
    cod_produto = input("Código do produto: [enter para sair]").strip()
    if not cod_produto:
        break
    if cod_produto not in produtos:
        print("Codigo inválido tente novamente.")
        continue
    quantidade = int(input("Quantas Unidades?:").strip())
    compra.items["items"].append([cod_produto, quantidade])

total_items = len(compra.items["items"])
print(f"Olá, {compra.cliente}")
print(f"No seu carrinho de compras tem {total_items} item.")
print(f"O total da compra é {compra.calcula_total(produtos):.2f}")
