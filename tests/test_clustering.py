import numpy as np
from clustering import aplicar_kmeans


def testar_aplicar_kmeans_retorna_labels_e_centros():
    # Dados simples
    dispositivos = np.array([
        [1, 2],
        [1, 4],
        [10, 2],
        [10, 4]
    ])

    labels, centros = aplicar_kmeans(dispositivos, n_clusters=2)

    # Verifica se retornou algo
    assert labels is not None
    assert centros is not None

    # Verifica tamanho dos resultados
    assert len(labels) == len(dispositivos)
    assert len(centros) == 2


def testar_aplicar_kmeans_clusters_corretos():
    dispositivos = np.array([
        [1, 2],
        [1, 4],
        [10, 2],
        [10, 4]
    ])

    labels, _ = aplicar_kmeans(dispositivos, n_clusters=2)

    # Deve existir exatamente 2 clusters
    assert len(set(labels)) == 2


def testar_aplicar_kmeans_com_um_cluster():
    dispositivos = np.array([
        [1, 2],
        [2, 3],
        [3, 4]
    ])

    labels, centros = aplicar_kmeans(dispositivos, n_clusters=1)

    assert len(set(labels)) == 1
    assert len(centros) == 1