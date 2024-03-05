import os

restaurantes = ['Pizzaria', 'Sushi']

# Abertura do app
def nome_programa():
    print("𝙱𝚎𝚖 𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝙸𝙳𝚒𝚗𝚗𝚎𝚛\n")

# Print das funcionalidades do app
def opcoes():
    print("1 - Cadastrar restaurante\n2 - Listar restaurante\n3 - Ativar restaurante\n4 - Sair do app")

#Funcao para cadastrar restaurantes no sistema
def cadastrar_restaurantes():
    exibir_subtitulo("Cadastrar restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi adicionado com sucesso")
    voltar_ao_menu()

#Funcao para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes\n")

    for restaurante in restaurantes:
        print(restaurante)
    voltar_ao_menu()

def voltar_ao_menu():
    input("\nDigite alguma tecla para voltar a tela inicial ")
    sistema()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)


# Logica para escolha da funcionalidade   
def escolha_opcoes():
    escolha = int(input("Escolha uma das opcoes: "))

    if escolha == 1:
        cadastrar_restaurantes()
    elif escolha == 2:
        listar_restaurantes()
    elif escolha == 3:
        os.system("cls")
        print("Ativando Restaurantes")
    elif escolha == 4:
        os.system("cls")
        print("Saindo do app")
    else:
        print("\nOpção invalida")
    
def sistema():
    os.system("cls")
    nome_programa()
    opcoes()
    escolha_opcoes()

if __name__ == "__main__":
    sistema()

