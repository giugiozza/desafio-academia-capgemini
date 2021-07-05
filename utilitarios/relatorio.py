from utilitarios.estruturas import MENU_RELATORIOS
from utilitarios.banco_de_dados import *
from utilitarios.common import *
from calculadora import calculadora


def listar_relatorios(connection, query, filtros):
    with connection:
        valor = 0
        visualizacoes = 0
        cliques = 0
        compartilhamentos = 0

        # lista todos os registros
        if filtros is None:
            retorno = connection.execute(RELATORIO_TOTAL)
            calculadora(retorno)

            if (connection.execute(query).fetchall()):
                pass
                # TODO: inserir valores

        elif filtros.count() == 1:
            connection.execute(query, (filtros))
            valor = 0
            visualizacoes = 0
            cliques = 0
            compartilhamentos = 0

        elif filtros.count() == 2:
            connection.execute(query, (filtros[0], filtros[1]))
            valor = 0
            visualizacoes = 0
            cliques = 0
            compartilhamentos = 0

        elif filtros.count() == 3:
            connection.execute(query, (filtros[0], filtros[1], filtros[3]))
            valor = 0
            visualizacoes = 0
            cliques = 0
            compartilhamentos = 0

        print("\t\tRelatório")
        print("=============================================")
        print(f'Valor total investido: {valor}')
        print(f'Quantidade máxima de visualizações: {visualizacoes}')
        print(f'Quantidade máxima de cliques: {cliques}')
        print(f'Quantidade máxima de compartilhamentos: {compartilhamentos}')
        print("=============================================")


def filtrar_relatorios(connection, filtro):

    # TODO trocar filtro para dicionário?

    if filtro == 1:
        cliente = input("\nDigite o nome do cliente: ")
        cliente = cliente + '%'
        listar_relatorios(connection, RELATORIO_POR_CLIENTE, cliente)

    if filtro == 2:
        data = []
        data[0] = input("\nDigite a data de início (dd/mm/aaaa): ")
        data[1] = input("\nDigite a data de término (dd/mm/aaaa): ")
        listar_relatorios(connection, RELATORIO_POR_DATA, data)

    if filtro == 3:
        filtros = []
        filtros[0] = input("\nDigite a data de início (dd/mm/aaaa): ")
        filtros[1] = input("\nDigite a data de término (dd/mm/aaaa): ")
        filtros[2] = input("\nDigite o nome do cliente: ")
        filtros[2] = filtros[2] + '%'
        listar_relatorios(connection, RELATORIO_POR_DATA_E_CLIENTE, filtros)


def relatorio(connection):

    opcao = str(input(MENU_RELATORIOS))
    if opcao.upper() == 'L':
        listar_relatorios(connection, SELECT_ALL, None)
        return 'M'

    elif opcao.upper() == 'P':
        filtro = str(input(MENU_RELATORIOS))
        filtrar_relatorios(connection, filtro)
        return 'M'

    elif opcao.upper() == 'M':
        return 'M'

    else:
        return 'M'
