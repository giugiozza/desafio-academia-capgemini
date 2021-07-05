from utilitarios.estruturas import *
from utilitarios.banco_de_dados import *
from utilitarios.cadastro import *
from utilitarios.relatorio import *


def main():

    connection = conecta_bd()
    cria_tabela(connection)

    while True:
        try:

            opcao = input(MENU_PRINCIPAL)

            if opcao.upper() == "I":
                retorno = cadastrar_anuncio(connection)
                if retorno == "N":
                    cadastrar_anuncio(connection)
                elif retorno == "M":
                    continue

            elif opcao.upper() == 'R':
                retorno = relatorio(connection)
                if retorno.upper() == 'M':
                    continue
                elif retorno.upper() == '':
                    pass
                    # TODO

            elif opcao.upper() == 'S':
                print("\nAté mais!")
                exit()

            else:
                print("\nOpção inválida. Selecione a letra correspondente entre as opções do menu.")

        except ValueError:
            print("Apenas letras são válidas. Tente novamente.") # TODO retirar?

    connection.close()


if __name__ == '__main__':
    main()
