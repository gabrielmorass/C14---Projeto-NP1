from sklearn.cluster import KMeans
from src.config import RANDOM_STATE, N_INIT


def aplicar_kmeans(dispositivos, n_clusters=4):
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=RANDOM_STATE,
        n_init=N_INIT
    )
    kmeans.fit(dispositivos)

    labels = kmeans.labels_
    centros = kmeans.cluster_centers_

    return labels, centros