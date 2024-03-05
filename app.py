import os

restaurantes = [{'nome': 'Roxy', 'categoria': 'Gourmet', 'ativo': False}, 
                {'nome': 'Famiglia', 'categoria': 'Italiana', 'ativo': True},
                {'nome': 'Forneria', 'categoria': 'Pizzaria', 'ativo': False}]

# Abertura do app
def nome_programa():
    print("𝙱𝚎𝚖 𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝙸𝙳𝚒𝚗𝚗𝚎𝚛\n")

# Print das funcionalidades do app
def opcoes():
    print("1 - Cadastrar restaurante\n2 - Listar restaurante\n3 - Alterar Status do restaurante\n4 - Sair do app")

#Funcao para cadastrar restaurantes no sistema
def cadastrar_restaurantes():
    exibir_subtitulo("Cadastrar restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria_restaurante, 'ativo': False}

    restaurantes.append(dados_restaurante)

    print(f"O restaurante {nome_restaurante} foi adicionado com sucesso!")
    voltar_ao_menu()


#Funcao para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes\n")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:

        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria'] 
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f"{nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu()

# Funcao para alterar o status do restaurante
def alterar_status():
    exibir_subtitulo("Alterando status do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (f"O restaurante {nome_restaurante} foi ativado com sucesso." 
                    if restaurante['ativo'] 
                    else f"O restaurante {nome_restaurante} foi desativado com sucesso.")
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")
    voltar_ao_menu()

def voltar_ao_menu():
    input("\nDigite alguma tecla para voltar a tela inicial ")
    sistema()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)


# Logica para escolha da funcionalidade   
def escolha_opcoes():
    escolha = int(input("\nEscolha uma das opções: "))

    if escolha == 1:
        cadastrar_restaurantes()
    elif escolha == 2:
        listar_restaurantes()
    elif escolha == 3:
        os.system("cls")
        alterar_status()
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

