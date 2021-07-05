import re
from utilitarios.banco_de_dados import *
from utilitarios.estruturas import *
from utilitarios.common import *


def validar_dados(anuncio):
    '''
    Itera sobre os dados do anúncio e valida
    se todos os campos foram preenchidos.
    '''

    for k, v in anuncio.__dict__.items():
        if v == "":
            print("Erro no cadastro: todos os dados devem ser preenchidos.")
            return False

        else:
            return True


def inserir_dados():
    print("\n*** Cadastro de Anúncio ***\n")

    anuncio = Anuncio(
        str(input("Nome do anúncio: ")),
        str(input("Nome do cliente: ")),
        str(input("Data de início do anúncio (dd/mm/aaaa): ")),
        str(input("Data de término do anúncio (dd/mm/aaaa): ")),
        str(input("Investimento diário: R$"))
    )

    return anuncio


def validar_datas(data_de_inicio, data_de_termino):
    data_de_inicio = (datetime.strptime(data_de_inicio, "%d/%m/%Y"))
    data_de_termino = (datetime.strptime(data_de_termino, "%d/%m/%Y"))

    if data_de_inicio > data_de_termino:
        print("\nA data de início deve ser anterior à data de término.")
        return False

    data_de_inicio = str(data_de_inicio)
    data_de_termino = str(data_de_termino)

    return True


def cadastrar_anuncio(connection):
    # TODO
    # exceptions de valor vazio
    # fazer trim da string
    try:
        anuncio = inserir_dados()

        if not (validar_dados(anuncio)):
            return (input(SUBMENU).upper())

        if not (validar_datas(anuncio.data_de_inicio, anuncio.data_de_termino)):
            return (input(SUBMENU).upper())

        confirma = confirmar("o cadastro")

        if not confirma:
            return (input(SUBMENU).upper())

        elif confirma:
            if insere_na_tabela(connection, anuncio) is None:
                print("\nErro na inserção dos dados. Tente novamente.\n")
                return "N"

        print("\nCadastro efetuado com sucesso!")
        return "M"

    except ValueError:
        print("\nAnúncio contém dado(s) inválido(s).")
        return (input(SUBMENU)).upper()
