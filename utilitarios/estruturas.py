# Menus
MENU_PRINCIPAL = ("""
***** MENU DE ANÚNCIOS *****

Selecione uma das opções:
[ I ] Inserir novo Anúncio
[ R ] Gerar Relatório
[ S ] Sair

> """)


SUBMENU = ('''
Operação cancelada.

Selecione uma das opções:
[ M ] Voltar ao menu principal
[ N ] Tentar novamente

> ''')


MENU_RELATORIOS = ("""
***** RELATÓRIOS *****

Selecione uma das opções:
[ L ] Listar todos os Anúncios
[ P ] Pesquisar Anúncios
[ M ] Voltar ao Menu Principal

> """)


MENU_FILTROS = ("""
Deseja filtrar os relatórios por:
[ C ] Cliente
[ T ] Intervalo de Tempo
[ A ] Ambos

> """)


# Classes
class Anuncio:
    def __init__(self, nome, cliente, data_de_inicio, data_de_termino, investimento_diario):
        self.nome = nome
        self.cliente = cliente
        self.data_de_inicio = data_de_inicio
        self.data_de_termino = data_de_termino
        self.investimento_diario = investimento_diario
