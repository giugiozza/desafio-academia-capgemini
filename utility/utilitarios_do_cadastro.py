from utility.estruturas import *


def submenu_cadastro():
    opcao = int(input('''
Operação cancelada.

Escolha:
[ 1 ] Tentar novamente
[ 2 ] Voltar ao menu principal
'''))
    return opcao


def cadastro_anuncio():
    # TODO
    # exceptions de valor vazio
    # fazer trim da string
    while True:
        try:
            print("\n*** Cadastro de Anúncio ***\n")
            nome = str(input("Nome do anúncio: "))
            cliente = str(input("Nome do cliente: "))
            data_de_inicio = str(input("Data de início do anúncio (dd/mm/aaaa): "))
            data_de_termino = str(input("Data de término do anúncio (dd/mm/aaaa): "))
            investimento_diario = float(input("Investimento diário (R$): "))

            anuncio = Anuncio(nome, cliente, data_de_inicio, data_de_termino, investimento_diario)

            confirma = ""
            while confirma.upper() != "S" and confirma.upper() != "N":
                confirma = input("\nConfirma o cadastro (S/N)? ")
                if confirma.upper() == "N":
                    return submenu_cadastro()
                elif confirma.upper() == "S":
                    # TODO
                    # colocar no BD
                    # data_inicio.strftime("%d/%m/%Y").isoformat() -> '2002-12-04'
                    print("\nCadastro efetuado com sucesso!")
                    repetir = input('\nDigite 1 para cadastrar outro anúncio ou qualquer outro valor para voltar ao menu principal.\n')
                    if repetir == '1':
                        # TODO
                        # criar classe/dicionario de menu para padronizar os retornos
                        return 1
                    else:
                        return 2
                else:
                    print("Digite 'S' para Sim e 'N' para não.\n")
        except ValueError:
            print("O valor inserido não é válido. Tente novamente.\n")
