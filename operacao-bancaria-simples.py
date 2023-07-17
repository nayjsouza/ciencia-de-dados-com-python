# Operação de Depósito:
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;
# Perguntar para o usuário o valor que deseja depositar.
# Operação de Saque:
# Permitidos realizar 3 saques diários com valor limite de R$ 500;
# Todos os saques devem ser armazenados em uma variável e exibido na operação de extrato.
# Operação de Extrato:
# Deve ser listado todos os valores de saque e depósito, no fim deve ser exibido o valor total da conta;

menu= '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = input (menu)

    if opcao == "d":
        valor = float(input("Informar o valor que deseja depositar R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Valor inválido")

    elif opcao == "s":
        valor = float(input("Informar o valor que deseja sacar R$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falho! Você não tem saldo suficiente")
        
        elif excedeu_limite:
            print("Operação falho! Você execdeu o valor limite para saque")
        
        elif excedeu_saque:
            print("Operação falhou! Você excedeu o número de saques diário")
        
        elif valor > 0:

            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        
        else:
            print("Valor inválido")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foi realizada nenhuma movimentação." if not extrato else extrato)
        print(f"\nValor: R$ {saldo:.2f}")
        print("===============================")
    
    elif opcao == "q":
        break

    else:
       print("Operação inválida, por favor digite novamente a opção desejada.")
