import os

projetos = {}

def adicionar_projeto(nome, status):
    projetos[nome] = status
    print("\nProjeto adicionado com sucesso!")

def atualizar_projeto(nome):
    if nome in projetos:
        novo_status = input("\nInforme o novo status do projeto: ")
        projetos.update({nome: novo_status})

        print("\nProjeto atualizado com sucesso!")
    else:
        print(f"\nO projeto {nome} não existe na lista.")

def exibir_projetos():
    if not projetos: 
        print("Não há projetos cadastrados.")
    else:
        print("Lista de projetos")
        for nome, status in projetos.items():
            print(f"\nProjeto: {nome}\nStatus: {status}")

def localizar_projeto(nome): 
    if nome in projetos:
        print(f"\nProjeto: {nome}\nStatus: {projetos[nome]}")
    else:
        print(f"\nO projeto {nome} não existe na lista.")


def excluir_projeto(nome):
    if nome in projetos:
        projetos.pop(nome)
        print(f"\nProjeto removido com sucesso!")
    else:
        print(f"\nO projeto {nome} não existe na lista.")

def limpar_console():
    os.system('cls')
    os.system('clear')

def pausar_console():
    return input("\nPressione Enter para continuar...")

def validar_nome(nome):
    if nome.strip() == "":
        return validar_nome(input("Nome não pode ficar em branco, tente novamente:"))
    elif nome in projetos: 
        return validar_nome(input("Esse projeto já existe na lista, tente novamente:"))
    else:
        return nome
    
while True:
    limpar_console()
    print("Cadastro de projetos")
    print("1 - Cadastrar")
    print("2 - Atualizar status")
    print("3 - Listar")
    print("4 - Localizar por nome")
    print("5 - Excluir")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    limpar_console()
    
    match opcao:
        case '1':
            print("Digite os dados do novo projeto")

            nome = validar_nome(input("Nome: "))
            status = input("Status: ")
            adicionar_projeto(nome, status)

            pausar_console()

        case '2':
            nome = input("Digite o nome do projeto que você deseja atualizar:")
            atualizar_projeto(nome)

            pausar_console()

        case '3':  
            exibir_projetos()
            pausar_console()

        case '4':
            nome = input("Digite o nome do projeto que você deseja localizar:")
            localizar_projeto(nome)
            pausar_console()

        case '5':
            if not projetos: 
                print("Não há projetos cadastrados.")
            else:
                print("Digite o nome do projeto que você deseja excluir:")

                nome = input("Nome: ")
                excluir_projeto(nome)

            pausar_console()

        case '0': 
            print("\nSaindo do programa.")
            break

        case _:
            print("\nOpção inválida!")