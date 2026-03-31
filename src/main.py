from config import (
    ARQUIVO_CSV,
    N_CLUSTERS,
    SET_ESCOLHIDO,
    SUBSET_ESCOLHIDO
)

from data_loader import carregar_dispositivos
from clustering import aplicar_kmeans
from plotting import plotar_clusters
from reporting import imprimir_dispositivos_por_cluster


if __name__ == "__main__":
    df, dispositivos = carregar_dispositivos(
        ARQUIVO_CSV,
        set_num=SET_ESCOLHIDO,
        subset_num=SUBSET_ESCOLHIDO
    )

    labels, centros = aplicar_kmeans(dispositivos, n_clusters=N_CLUSTERS)

    plotar_clusters(
        dispositivos,
        labels,
        centros,
        N_CLUSTERS,
        titulo=f"K-Means - Set {SET_ESCOLHIDO}, Subset {SUBSET_ESCOLHIDO}"
    )

    imprimir_dispositivos_por_cluster(df, labels, N_CLUSTERS)