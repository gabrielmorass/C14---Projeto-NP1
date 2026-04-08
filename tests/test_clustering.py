import pytest
import numpy as np

from clustering import aplicar_kmeans



def gerar_dados_simples():
    return [
        [1, 2],
        [1, 3],
        [10, 10],
        [10, 11]
    ]


def test_retorno_labels_e_centros():
    dados = gerar_dados_simples()

    labels, centros = aplicar_kmeans(dados, n_clusters=2)

 
    assert len(labels) == len(dados)

  
    assert len(centros) == 2


def test_tipo_retorno():
    dados = gerar_dados_simples()

    labels, centros = aplicar_kmeans(dados, n_clusters=2)

    assert isinstance(labels, np.ndarray)
    assert isinstance(centros, np.ndarray)



def test_consistencia_resultados():
    dados = gerar_dados_simples()

    labels1, centros1 = aplicar_kmeans(dados, 2)
    labels2, centros2 = aplicar_kmeans(dados, 2)

    assert (labels1 == labels2).all()
    assert np.allclose(centros1, centros2)



def test_numero_clusters():
    dados = gerar_dados_simples()

    _, centros = aplicar_kmeans(dados, n_clusters=3)

    assert len(centros) == 3


def test_entrada_invalida():
    with pytest.raises(Exception):
        aplicar_kmeans(None)