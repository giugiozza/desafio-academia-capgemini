import os


def cadastrar_anuncio():
    pass


def gerar_relatorio():
    pass


def menu():
    opcao = int(input("""
***** MENU DE ANÚNCIOS *****

  [ 1 ] Cadastrar Anúncio
  [ 2 ] Gerar Relatório
  [ 3 ] Sair

Selecione uma opção: """))

    if opcao == 1:
        cadastrar_anuncio()
    elif opcao == 2:
        gerar_relatorio()
    elif opcao == 3:
        print("Até mais!")
        exit()
    else:
        print("--> Essa opção não é válida! :(\nTente novamente.\n")
        menu()
