import os

# Abertura do app
print("𝙱𝚎𝚖 𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝙸𝙳𝚒𝚗𝚗𝚎𝚛\n")


def opcoes():
    print("1 - Cadastrar restaurante\n2 - Listar restaurante\n3 - Ativar restaurante\n4 - Sair do app")

    
def escolha_opcoes():
    escolha = int(input("Escolha uma das opcoes: "))

    if escolha == 1:
        os.system("cls")
        print("Cadastro de restaurante")
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
        print("Opção invalida")
    
def sistema():
    opcoes()
    escolha_opcoes()

if __name__ == "__main__":
    sistema()

