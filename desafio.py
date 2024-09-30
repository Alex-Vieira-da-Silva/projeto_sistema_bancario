# Menu de opções para o usuário
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

# Inicialização das variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do sistema bancário
while True:

    # Exibe o menu e lê a opção escolhida pelo usuário
    opcao = input(menu)

    # Opção de depósito
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de saque
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        # Verifica se o valor do saque excede o saldo disponível
        excedeu_saldo = valor > saldo

        # Verifica se o valor do saque excede o limite permitido
        excedeu_limite = valor > limite

        # Verifica se o número de saques diários já foi atingido
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Opção de extrato
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Opção de sair
    elif opcao == "4":
        break

    # Caso a opção seja inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")