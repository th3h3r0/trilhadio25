# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:

if preco == 100:
    novo_valor = preco *  (1 - 10/100)
    print(f"{novo_valor:.2f}\n")

elif preco == 200:
    novo_valor = preco * (1 - 20/100)
    print(f"{novo_valor:.2f}\n")

if preco == 50:
    novo_valor = preco
    print(f"{novo_valor:.2f}\n")