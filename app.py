from datetime import datetime
saldo  = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


menu = (f"""
Saldo atual: R${saldo}
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
""")


while True:
    menu = (f"""
Saldo atual: R${saldo:.2f}
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
    """)
    opcao = input(menu)

    if opcao == "1":
        deposito = int(input("Informe o valor que deseja depósitar: R$"))
        if deposito <= 0:
            print("O valor informado não é válido!")
        else:
            saldo += deposito
            extrato += (f"Você realizou um depósito de R$:{deposito}\nData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            print("Deposito realizado com sucesso")
    elif opcao == "2":
        
        saque = int(input("Qual valor deseja sacar: R$"))

        excedeu_saldo =  saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Seu limite de saque é de R$ 500.00")
        elif excedeu_saques:
            print("Você atingiu o limite de saques diarios")
        elif saque > 0:
            saldo -= saque
            extrato += (f"Você realizou uma retirada de R$:{saque:.2f}\nData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor informado, Inválido")
            
    elif opcao == "3":
        print(f"\n{'#'*6} EXTRATO {'#'*6}")
        print("Não foram realizadas tranzações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"{'#'*21}")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Digite uma opção válida.")


# print(f"\n{'#'*6} EXTRATO {'#'*6}")
# print("Não foram realizadas tranzações." if not extrato else extrato)
# print(f"n\Saldo: R$ {saldo:.2f}")
# print(f"{'#'*21}")