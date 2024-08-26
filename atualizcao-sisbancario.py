usuarios = []
contas_correntes = []

def menu_principal():
    menu = '''
          ################## -MENU- ########################

                        [1] - Depositar
                        [2] - Sacar
                        [3] - Extrato
                        [4] - Criar Usuário
                        [5] - Criar Conta Corrente
                        [6] - Listar Contas Correntes
                        [7] - Sair

          ####################################################
                        
                        Escolha uma opção: '''
    return input(menu).strip()

def criar_usuario():
    global usuarios
    cpf = input("Informe o CPF (somente números): ").strip()
    if buscar_usuario(cpf):
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/estado): ").strip()
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def buscar_usuario(cpf):
    global usuarios
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta_corrente(numero_conta, agencia):
    global contas_correntes
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = buscar_usuario(cpf)
    
    if usuario:
        numero_conta += 1
        contas_correntes.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        print("Conta corrente criada com sucesso!")
        return numero_conta
    else:
        print("Usuário não encontrado! Crie um usuário antes de criar uma conta corrente.")
        return numero_conta

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print('OPERAÇÃO FALHOU! Valor informado não é válido!')
    return saldo, extrato

def sacar(valor, saldo, extrato, limite, numero_de_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("OPERAÇÃO FALHOU! Excedeu o saldo da conta!")
    elif valor > limite:
        print("OPERAÇÃO FALHOU! Excedeu o limite de saque da conta!")
    elif numero_de_saques >= LIMITE_SAQUES:
        print("OPERAÇÃO FALHOU! Excedeu o número de saques permitidos!")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_de_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("OPERAÇÃO FALHOU! Informe um valor válido.")
    return saldo, extrato, numero_de_saques

def exibir_extrato(saldo, extrato):
    print("\n" + "=" * 20 + " EXTRATO " + "=" * 20)
    if extrato:
        for movimento in extrato:
            print(movimento)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=" * 40)

def listar_contas():
    global contas_correntes
    if contas_correntes:
        print("\nListagem de Contas Correntes:\n")
        for conta in contas_correntes:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {usuario['nome']} | CPF: {usuario['cpf']}\n")
    else:
        print("Nenhuma conta corrente cadastrada.")


AGENCIA = "0001"
numero_conta = 0


saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = menu_principal()

    if opcao == '1':
        try:
            valor = float(input("Informe o valor do depósito: ").strip())
            saldo, extrato = depositar(valor, saldo, extrato)
        except ValueError:
            print("OPERAÇÃO INVÁLIDA! Informe um valor numérico válido para o depósito.")
    
    elif opcao == '2':
        try:
            valor = float(input("Informe o valor do saque: ").strip())
            saldo, extrato, numero_de_saques = sacar(valor, saldo, extrato, limite, numero_de_saques, LIMITE_SAQUES)
        except ValueError:
            print("OPERAÇÃO INVÁLIDA! Informe um valor numérico válido para o saque.")
    
    elif opcao == '3':
        exibir_extrato(saldo, extrato)
    
    elif opcao == '4':
        criar_usuario()
    
    elif opcao == '5':
        numero_conta = criar_conta_corrente(numero_conta, AGENCIA)
    
    elif opcao == '6':
        listar_contas()
    
    elif opcao == '7':
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("OPERAÇÃO INVÁLIDA! Por favor, selecione uma opção válida do menu.")
