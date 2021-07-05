import sys


VISUALIZACOES_POR_COMPARTILHAMENTO = 30


def calculadora(investimento_diario):

    clique_max, compartilhamento_max, visualizacao_max = 0

    n_vis = []
    n_compartilhamentos = []
    n_cliques = []

    n_vis[0] = investimento_diario * VISUALIZACOES_POR_COMPARTILHAMENTO

    for i in range(0, 4):
        if i != 0:
            n_vis[i] = n_compartilhamentos[i - 1] * 40

        n_cliques[i] = visualizacao_max[i] * 0.12
        if i != 3:
            n_compartilhamentos[i] = n_cliques[i] * 0.15
            compartilhamento_max += n_compartilhamentos[i]
        visualizacao_max += n_vis[i]
        clique_max += n_cliques[i]

        return 
