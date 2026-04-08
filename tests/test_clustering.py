import numpy as np

from src.clustering import aplicar_kmeans


def test_aplicar_kmeans_retorna_labels_e_centros():
    dispositivos = np.array([
        [1, 1],
        [1, 2],
        [9, 9],
        [9, 8],
    ])

    labels, centros = aplicar_kmeans(dispositivos, n_clusters=2)

    assert len(labels) == len(dispositivos)
    assert centros.shape == (2, 2)


def test_aplicar_kmeans_gera_quantidade_correta_de_clusters():
    dispositivos = np.array([
        [1, 1],
        [1, 2],
        [9, 9],
        [9, 8],
        [5, 5],
        [5, 6],
    ])

    labels, centros = aplicar_kmeans(dispositivos, n_clusters=3)

    assert len(set(labels)) == 3
    assert len(centros) == 3


def test_aplicar_kmeans_com_mesmo_random_state_e_deterministico():
    dispositivos = np.array([
        [1, 1],
        [1, 2],
        [9, 9],
        [9, 8],
    ])

    labels1, centros1 = aplicar_kmeans(dispositivos, n_clusters=2)
    labels2, centros2 = aplicar_kmeans(dispositivos, n_clusters=2)

    assert np.array_equal(labels1, labels2)
    assert np.allclose(centros1, centros2)


def test_aplicar_kmeans_quando_clusters_maiores_que_amostras_gera_erro():
    dispositivos = np.array([
        [1, 1],
        [2, 2],
    ])

    import pytest
    with pytest.raises(ValueError):
        aplicar_kmeans(dispositivos, n_clusters=3)