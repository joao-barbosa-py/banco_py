from datetime import datetime
import textwrap

def menu(saldo):
    saldo_atualizado = saldo
    return input(f"""
    Saldo atual: R${saldo_atualizado:.2f}
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Novo Usuário
    [5] - Nova Conta
    [6] - Listar Contas
    [7] - Sair
    """)

def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito realizado com sucesso!"
    else:
        print("\nEssa operação falhou!")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo =  valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Seu limite de saque é de R$ 500.00")
    elif excedeu_saques:
        print("Você atingiu o limite de saques diarios")
    elif valor > 0:
        saldo -= valor
        extrato += (f"Você realizou uma retirada de R$:{valor:.2f}\nData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Valor informado, Inválido") 

    return saldo, extrato   

def extrato_visual(saldo,/,*, extrato):

    print(f"\n{'#'*6} EXTRATO {'#'*6}")
    print("Não foram realizadas tranzações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(f"\n{'#'*21}")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def new_user(usuarios):
    cpf = input("Informe o CPF (Apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe um usuário com esse CPF!")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento=input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado ): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def new_account(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo  = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu(saldo)

        if opcao == "1":
            valor = float(input("Informe o valor que deseja depósitar: R$"))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "2":     
            valor = int(input("Qual valor deseja sacar: R$"))
            saldo, extrato = saque(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                numero_saques= numero_saques,
                limite_saques= LIMITE_SAQUES,
            )       
        elif opcao == "3":
            extrato_visual(saldo, extrato=extrato) 
        elif opcao == "4":
            new_user(usuarios)  
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = new_account(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta) 
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Digite uma opção válida.")

main()

# print(f"\n{'#'*6} EXTRATO {'#'*6}")
# print("Não foram realizadas tranzações." if not extrato else extrato)
# print(f"n\Saldo: R$ {saldo:.2f}")
# print(f"{'#'*21}")