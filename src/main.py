from config import (
    ARQUIVO_CSV,
    N_CLUSTERS,
    SET_ESCOLHIDO,
    SUBSET_ESCOLHIDO
)
from data_loader import carregar_dispositivos
from clustering import aplicar_kmeans
from plotting import plotar_clusters
from reporting import (
    gerar_relatorio_clusters,
    salvar_relatorio_csv,
    imprimir_dispositivos_por_cluster
)

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
        titulo=f"K-Means - Set {SET_ESCOLHIDO}, Subset {SUBSET_ESCOLHIDO}",
        salvar_em="results/clusters.png"
    )

    df_resultado = gerar_relatorio_clusters(df, labels)
    salvar_relatorio_csv(df_resultado, "results/cluster_report.csv")
    imprimir_dispositivos_por_cluster(df_resultado, N_CLUSTERS)

    print("\nResultados salvos em results/")