def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    return

def deposito(saldo, valor, extrato, /):
    if (valor <= 0):
        return False
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato

def extrato(saldo, /, *, extrato):
    return

def endereco(logradouro, nro, bairro, cidade, sigla_estado):
    return 

def cria_usuario(nome, nascimento, cpf):
    return

def cria_conta_corrente(usuario):
    AGENCIA = "0001"
    return

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato_string = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
       
       valor = float(input("Informe o valor do depósito: "))
       resultado_deposito = deposito(saldo, valor, extrato_string)
       if (resultado_deposito != False):
           saldo = resultado_deposito[0]
           extrato_string = resultado_deposito[1]
       else:
           print("Operação falhou! O valor informado é inválido.")
           
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato_string += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato_string else extrato_string)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
