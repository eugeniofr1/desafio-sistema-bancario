def menu(): 
    menu = """\n
    ======== MENU ========
    [1]\t Depositar
    [2]\t Sacar
    [3]\t Extrato
    [4]\t Nova conta
    [5]\t Listar contas
    [6]\t Novo usuário
    [0]\t Sair
    => """
    return (int(input(menu)))

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n Depósito realizado com sucesso!")
    else:
        print("\n Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
    elif valor > limite_saques:
        print("Operação falhou! O valor do saque excede o limite.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    elif numero_saques > LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

while True:
    opcao = menu()

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)
        

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )
        
    
    elif opcao == 3:
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")