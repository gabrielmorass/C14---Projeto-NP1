import pandas as pd

from src.reporting import imprimir_dispositivos_por_cluster


def test_imprimir_dispositivos_por_cluster_exibe_clusters(capsys):
    df = pd.DataFrame({
        "Device_ID": [1, 2, 3, 4],
        "X": [1, 2, 8, 9],
        "Y": [1, 2, 8, 9],
    })
    labels = [0, 0, 1, 1]

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    saida = capsys.readouterr().out
    assert "Cluster 1:" in saida
    assert "Cluster 2:" in saida


def test_imprimir_dispositivos_por_cluster_exibe_device_ids(capsys):
    df = pd.DataFrame({
        "Device_ID": [10, 20],
        "X": [5, 6],
        "Y": [7, 8],
    })
    labels = [0, 1]

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    saida = capsys.readouterr().out
    assert "10" in saida
    assert "20" in saida


def test_imprimir_dispositivos_por_cluster_adiciona_coluna_sem_alterar_df_original():
    df = pd.DataFrame({
        "Device_ID": [1, 2],
        "X": [1, 2],
        "Y": [3, 4],
    })
    labels = [0, 1]

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    assert "Cluster" not in df.columns