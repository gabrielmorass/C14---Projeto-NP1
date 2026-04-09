from src.config import (
    ARQUIVO_CSV,
    N_CLUSTERS,
    SET_ESCOLHIDO,
    SUBSET_ESCOLHIDO
)
from src.data_loader import carregar_dispositivos
from src.clustering import aplicar_kmeans
from src.plotting import plotar_clusters
from src.reporting import (
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
    imprimir_dispositivos_por_cluster(df, labels, N_CLUSTERS)

    print("\nResultados salvos em results/")