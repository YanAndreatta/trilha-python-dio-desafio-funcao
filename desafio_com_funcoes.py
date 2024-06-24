import textwrap


def menu():
    opcoes_menu = """

[c] Criar Usuário
[cc] Criar Conta Corrente
[lc] Listar Contas
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    return input(textwrap.dedent(opcoes_menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação de saque realizada com sucesso!")

        return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"    
        print("Depósito efetuado com sucesso!")
        
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
 
def cria_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuário já existe")
        return
    
    nome = input("Informe o nome: ")
    nascimento = input("Informe a data de nascimento (DD-MM-YYYY): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def cria_conta_corrente(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF (somente números): ")
    usuario_filtrado = filtrar_usuario(cpf, usuarios)
    
    if usuario_filtrado:
        contas.append({"agencia": agencia, "conta": numero_conta, "usuario": usuario_filtrado })
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado")

def listar_contas(contas):
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['conta']}")
        print(f"Usuário: {conta['usuario']['nome']}")
        print("==========================================")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato_string = ""
    numero_saques = 0

    while True:

        opcao = menu()

        if opcao == "d":
        
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato_string = deposito(saldo, valor, extrato_string)
            
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato_string, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato_string, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
            
        elif opcao == "e":
            extrato(saldo, extrato=extrato_string)
        
        elif opcao == "c":
            cria_usuario(usuarios)
            
        elif opcao == "cc":
            conta = len(contas) + 1
            cria_conta_corrente(AGENCIA, conta, usuarios, contas)
        
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()