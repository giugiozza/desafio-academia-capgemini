import sqlite3
from utility.utilitarios_do_menu import *


def main():
    while True:
        try:
            opcao = menu()
            if not opcao:
                raise Exception
            elif opcao == 1:
                if cadastro_anuncio() == 1:
                    cadastro_anuncio()
                elif cadastro_anuncio() == 2:
                    continue
                else:
                    print("Opção inválida! :(")
            elif opcao == 2:
                pass
            elif opcao == 3:
                print("\nAté mais!")
                exit()
            else:
                print("\nOpção inválida. Selecione um número dentre as opções do menu.")
        except ValueError:
            print("Apenas números são válidos. Tente novamente.")


if __name__ == '__main__':
    main()
