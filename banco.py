import os


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    LIMITES_SAQUES = 3
    contas = []
    usuarios = []
    AGENCIA = "0001"

    while True:
        opcao = menu()
        os.system('cls')
        if opcao == "q":
            break

        elif opcao == "d":
            valor = float(input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor, 
                extrato = extrato,
                limite = limite,
                numeros_saques = numeros_saques,
                limites_saques = LIMITES_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)

def menu(): 
    menu = """\n
    =====MENU=====
    [D]epositar
    [S]aque
    [E]xtrato
    [NC]Nova Conta
    [LC]Listar contas
    [NU]Novo Usuário
    [Q]Sair
    """
    return input(menu).lower()


def depositar(saldo, valor, extrato, /):
    if valor < 1:
        print("Valor invalido!")
    else:
        saldo += valor
        print("Depósito realizado com sucesso")
        extrato += f"Deposito R${valor:.2f}\n"
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numeros_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques > limites_saques
    if excedeu_saldo:
        print("Operação inválida! O saldo não é suficiente")
    elif excedeu_limite:
        print("Operação inválida! O limite do saque foi excedido")
    elif excedeu_saques:
        print("Operação inválida! O limites de saques foi excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque R${valor:.2f}\n"
        numeros_saques += 1
        print("Saque realizado com sucesso")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Nao foram realizadas movimentações" if not extrato else extrato) 
    print(f"Saldo: R$: {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Insira seu cpf(somente numeros): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Esse usuário já foi cadastrado")
        return
    nome = input("Insira seu nome completo: ")
    data_nascimento = input("Insira sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Insira seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"Agência: {conta['agencia']}\n C/C {conta['numero_conta']} \n Titular {conta['usuario']['nome']} "
        print("=" *100)
        print(linha)

main()