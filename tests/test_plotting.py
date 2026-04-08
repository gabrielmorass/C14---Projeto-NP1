import numpy as np
from unittest.mock import patch

from plotting import plotar_clusters


#  Dados falsos
def gerar_dados():
    dispositivos = np.array([
        [1, 2],
        [1, 3],
        [10, 10],
        [10, 11]
    ])

    labels = np.array([0, 0, 1, 1])
    centros = np.array([
        [1, 2.5],
        [10, 10.5]
    ])

    return dispositivos, labels, centros


#  Teste 1: verifica se funções do matplotlib são chamadas
@patch("matplotlib.pyplot.show")
@patch("matplotlib.pyplot.scatter")
@patch("matplotlib.pyplot.figure")
def test_plotagem_basica(mock_figure, mock_scatter, mock_show):
    dispositivos, labels, centros = gerar_dados()

    plotar_clusters(dispositivos, labels, centros, n_clusters=2)

    # figura criada
    mock_figure.assert_called_once()

    # scatter chamado (clusters + centroides)
    assert mock_scatter.call_count >= 3

    # show chamado
    mock_show.assert_called_once()


#  Teste 2: verifica número de clusters plotados
@patch("matplotlib.pyplot.scatter")
def test_numero_clusters_plotados(mock_scatter):
    dispositivos, labels, centros = gerar_dados()

    plotar_clusters(dispositivos, labels, centros, n_clusters=2)

   
    assert mock_scatter.call_count >= 3


#  Teste 3: não quebra com dados válidos
def test_execucao_sem_erro():
    dispositivos, labels, centros = gerar_dados()

    
    plotar_clusters(dispositivos, labels, centros, n_clusters=2)
