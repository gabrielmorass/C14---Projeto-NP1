import matplotlib.pyplot as plt
from config import X_LIM, Y_LIM


def plotar_clusters(dispositivos, labels, centros, n_clusters, titulo="K-Means"):
    plt.figure(figsize=(8, 8))

    for idx in range(n_clusters):
        cluster_points = dispositivos[labels == idx]
        plt.scatter(
            cluster_points[:, 0],
            cluster_points[:, 1],
            label=f"Cluster {idx + 1}"
        )

    plt.scatter(
        centros[:, 0],
        centros[:, 1],
        c="red",
        s=150,
        marker="X",
        label="Centroides"
    )

    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    plt.xlim(X_LIM)
    plt.ylim(Y_LIM)
    plt.show()