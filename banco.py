import os

menu = """
    [D]epositar
    [S]aque
    [E]xtrato
    [Q]Sair
"""
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu).lower()
    os.system('cls')
    if opcao == "q":
        break
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        if valor < 1:
            print("Valor invalido!")
        else:
            saldo += valor
            extrato += f"Deposito R${valor:.2f}\n"

    if opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        if LIMITES_SAQUES > 0:
            if valor < 0:
                print("Digite um valor valido")
            if valor > 500:
                print("O valor máximo é de R$500,00")
            if valor > saldo:
                print("Saldo insuficiente")
            if valor <= saldo and valor <= 500 and LIMITES_SAQUES > 0:
                saldo -= valor
                LIMITES_SAQUES -= 1
                extrato += f"Saque R${valor:.2f}\n"
        else:
            print("Limite atingido")

    if opcao == "e":
        print("Nao foram realizadas movimentações" if not extrato else extrato) 
        print(f"Saldo: R$: {saldo:.2f}")
    
    