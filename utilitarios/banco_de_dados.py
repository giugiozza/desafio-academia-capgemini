import sqlite3
from datetime import datetime
from utilitarios.estruturas import *


# queries
CREATE_TABLE = ('''
CREATE TABLE IF NOT EXISTS anuncios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cliente TEXT,
    data_de_inicio TEXT,
    data_de_termino TEXT,
    investimento_diario REAL);
''')

INSERT = ('''
INSERT INTO anuncios(nome, cliente, data_de_inicio, data_de_termino, investimento_diario)
    VALUES (?, ?, ?, ?, ?);
''')

SELECT_ALL = ('''
SELECT *
FROM anuncios
''')


RELATORIO_TOTAL = ('''
SELECT (SUM(investimento_diario)*(data_de_termino - data_de_inicio))
FROM anuncios
GROUP BY nome, cliente
''')


RELATORIO_POR_CLIENTE = ('''
SELECT *
FROM anuncios
WHERE cliente like ?
ORDER BY cliente, data_de_inicio;
''')


# relatório filtrado por data
RELATORIO_POR_DATA = ('''
SELECT *
FROM anuncios
WHERE (data_de_inicio >= ? AND data_de_termino <= ?)
ORDER BY cliente, data_de_inicio;
''')


# relatório filtrado por data E cliente
RELATORIO_POR_DATA_E_CLIENTE = ('''
SELECT *
FROM anuncios
WHERE (data_de_inicio >= ? AND data_de_termino <= ?)
AND cliente like ?
ORDER BY cliente, data_de_inicio;
''')





# funções
def conecta_bd():
    '''
    Inicializa a conexão com o banco de dados.
    '''

    return sqlite3.connect("dados.db")


def cria_tabela(connection):
    '''
    Cria a tabela de anúncios.
    Se a tabela já existe, não faz nada.
    '''

    with connection:
        return connection.execute(CREATE_TABLE).fetchall()


def insere_na_tabela(connection, anuncio):
    '''
    Formata as datas do anúncio para o tipo correspondente em SQL
    e insere o registro na tabela.
    '''
    # TODO: formatar datas para tipo do sql?

    with connection:
        return connection.execute(
            INSERT, (anuncio.nome, anuncio.cliente,
                     anuncio.data_de_inicio, anuncio.data_de_termino,
                     anuncio.investimento_diario)
        ).fetchall()
