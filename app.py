import os

# Abertura do app
def nome_programa():
    print("𝙱𝚎𝚖 𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝙸𝙳𝚒𝚗𝚗𝚎𝚛\n")

# Print das funcionalidades do app
def opcoes():
    print("1 - Cadastrar restaurante\n2 - Listar restaurante\n3 - Ativar restaurante\n4 - Sair do app")

def cadastrar_restaurantes():
    os.system("cls")
    print("Cadastro de restaurante\n")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    print(f"O restaurante {nome_restaurante} foi adicionado com sucesso\n")
    input("Digite alguma tecla para voltar a tela inicial ")
    voltar_ao_menu()

def voltar_ao_menu():
    os.system("cls")
    nome_programa()
    opcoes()
    escolha_opcoes()


# Logica para escolha da funcionalidade   
def escolha_opcoes():
    escolha = int(input("Escolha uma das opcoes: "))

    if escolha == 1:
        cadastrar_restaurantes()
    elif escolha == 2:
        os.system("cls")
        print("Listar Restaurantes")
    elif escolha == 3:
        os.system("cls")
        print("Ativando Restaurantes")
    elif escolha == 4:
        os.system("cls")
        print("Saindo do app")
    else:
        print("\nOpção invalida")
    
def sistema():
    nome_programa()
    opcoes()
    escolha_opcoes()

if __name__ == "__main__":
    sistema()

