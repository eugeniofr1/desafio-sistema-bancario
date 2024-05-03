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

LIMITE_SAQUES = 3
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

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
        
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    elif numero_saques > LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

     nome = input("Informe o nome completo: ") 
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (Rua, nº, cidade/sigla estado): ")

     usuarios.append({"nome":nome, "data_nascimentto": data_nascimento, "cpf":cpf, "endereço": endereco})

     print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Conta criada com sucesso! ")
          return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
    
     print("\n Usuário não encontrado, criação de conta encerrado!")

def listar_contas(contas):
     for conta in contas:
          print(f" Agência: {conta['agencia']}, Conta {conta['numero_conta']}, Titular {conta['usuario']['nome']}")

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

    elif opcao == 4:
         numero_conta = len(contas) + 1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)

         if conta:
              contas.append(conta)
    
    elif opcao == 5:
         listar_contas(contas)

    elif opcao == 6:
         criar_usuario(usuarios)
    
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")