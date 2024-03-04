# Abertura do app
print("𝙱𝚎𝚖 𝚟𝚒𝚗𝚍𝚘 𝚊𝚘 𝙸𝙳𝚒𝚗𝚗𝚎𝚛\n")

def opcoes():
    print("1 - Cadastrar restaurante\n2 - Listar restaurante\n3 - Ativar restaurante\n4 - Sair do app")
    escolha = int(input("Escolha uma das opcoes: "))

    if escolha == 1:
        print("Cadastro de restaurante")
    elif escolha == 2:
        print("Listar Restaurantes")
    elif escolha == 3:
        print("Ativando Restaurantes")
    elif escolha == 4:
        print("Saindo do app")
    else:
        print("Opção invalida")
    
opcoes()

