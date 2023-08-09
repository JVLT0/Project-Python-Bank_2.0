usuarios = []

def menu():
    print("==================||==================")
    return int(input("""
    [1] Cadastrar
    [2] Entrar
    [3] Sair
    """))

def menu1():
    print("==================||==================")
    return int(input("""
    [1] Sacar
    [2] Depositar
    [3] Extrato
    [4] Sair
    """))

def cadastro():
    print("==================||==================")
    nome = input("Digite o nome de usuario: ")
    senha = input("Crie uma senha: ")
    novo_usuario ={
        "nome_usuario": nome,
        "senha": senha,
        "saldo": 0,
        "limite": 500,
        "quantSaque": 0,
        "quantDeposito": 0
    }

    usuarios.append(novo_usuario)
    print("Usuario criado com sucesso")

def sacar(saldo, quantSaque, limite):
    print("==================||==================")
    print("Digite o valor que deseja sacar")
    saque = float(input())

    if(saque <= saldo + limite and quantSaque < 3):
        print("Saque autorizado")
        saldo -= saque
        quantSaque += 1

        return saldo, quantSaque
    else:
        print("Saque não autorizado")
        return saldo, quantSaque
        
def depositar(saldo, quantDeposito):
    print("==================||==================")
    print("Digite o valor do deposito")
    deposito = float(input())
    saldo += deposito
    quantDeposito += 1
    print("Deposito efetuado")

    return saldo, quantDeposito

def extrato(saldo, quantSaque, quantDeposito):
    print("==================||==================")
    print(f"""
        Saldo: R${saldo}
        Quantidade de Saques: {quantSaque}
        Quantidade de Depositos: {quantDeposito}
          """)

def main():
    opc = 0

    while opc != 3:
        opc = menu()
        if opc == 1:
            cadastro()

        elif opc == 2:
            print("==================||==================")
            nome = input("Digite seu nome de usuario: ")
            senha = input("Digite sua senha: ")

            usuario_encontrado = None
            for usuario in usuarios:
                if usuario['nome_usuario'] == nome and usuario['senha'] == senha:
                    usuario_encontrado = usuario
                    break
            
            if usuario_encontrado:
                print(f"Bem vindom, {usuario_encontrado['nome_usuario']}!")

                opc_01 = 0
                while opc_01 != 4:
                    opc_01 = menu1()

                    if opc_01 == 1:
                        saldo, quantSaque = sacar(usuario_encontrado['saldo'], usuario_encontrado['quantSaque'], usuario_encontrado['limite'])
                        usuario_encontrado['saldo'], usuario_encontrado['quantSaque'] = saldo, quantSaque
                        
                    elif opc_01 == 2:
                        saldo, quantDeposito = depositar(usuario_encontrado['saldo'], usuario_encontrado['quantDeposito'])
                        usuario_encontrado['saldo'], usuario_encontrado['quantDeposito'] = saldo, quantDeposito

                    elif opc_01 == 3:
                        extrato(usuario_encontrado['saldo'], usuario_encontrado['quantSaque'], usuario_encontrado['quantDeposito'])

                    elif opc_01 == 4:
                        print("Saindo...")
                        break
            else:
                print("Usuario não encontrado ou senha incorreta")

        elif(opc == 3):
            print("Saindo...")
            break

main()
   
