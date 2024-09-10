def sacar ():
    global saldo, numero_saques, extrato
    saque = float(input("\nValor que deseja sacar => "))
    if saque > 0:
        if saque <= saldo and numero_saques < LIMITE_SAQUES:
            saldo-=saque
            print(f"\nSaque de R$ {saque:.2f} realizado com sucesso!")
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques+=1
        elif saque > saldo:
            print("\nNão foi possível realizar o saquee, saldo insuficiente.")
        else:
            print("\nNão foi possível realizar o saquee, limite de saque diário atingido.")
    else:
        print("\nValor inválido!")

def depositar():
    global saldo, extrato
    deposito = float(input("\nValor que deseja depositar => "))
    if deposito > 0:
        saldo += deposito
        print(f"\nDepósito de R$ {deposito:.2f} realizado com sucesso!")
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("\nValor inválido!")

menu = '''

========= MENU =========

    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [0] - Sair

=>'''

saldo = 0.00
limite = 500.00
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("### Depósito ###")
        depositar()

    elif opcao == 2:
        print("### Sacar ###")
        sacar()

    elif opcao == 3:
        print("### Extrato ###")
        if extrato == " ":
            print("\nNão foi realizado nenhuma movimentação.")
        else:
            print(f"\n{extrato}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("###############")

    elif opcao == 0:
        print("### Sair ###")
        break

    else:
        print('Apresemte apenas uma das opções válidas!')