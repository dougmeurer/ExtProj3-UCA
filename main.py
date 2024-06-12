clientes = []

def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    sexo = input("Sexo (M/F): ")
    cpf = input("CPF: ")
    
    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'endereco': endereco,
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'cpf': cpf
    }
    
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!\n")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.\n")
    else:
        for i, cliente in enumerate(clientes):
            print(f"Cliente {i + 1}:")
            print(f"Nome: {cliente['nome']}")
            print(f"E-mail: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            print(f"Endereço: {cliente['endereco']}")
            print(f"Data de nascimento: {cliente['data_nascimento']}")
            print(f"Sexo: {cliente['sexo']}")
            print(f"CPF: {cliente['cpf']}\n")

def main():
    while True:
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            print("Até Logo!")
            break
        else:
            print("Ups! opção inválida. Tente novamente.\n")

main()