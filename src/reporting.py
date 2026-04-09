import os

def gerar_relatorio_clusters(df, labels):
    df_resultado = df.copy()
    df_resultado["Cluster"] = [label + 1 for label in labels]
    return df_resultado

def salvar_relatorio_csv(df_resultado, caminho_saida):
    os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)
    df_resultado.to_csv(caminho_saida, index=False)

def imprimir_dispositivos_por_cluster(df, labels, n_clusters):
    df_resultado = gerar_relatorio_clusters(df, labels)

    for idx in range(1, n_clusters + 1):
        cluster_df = df_resultado[df_resultado["Cluster"] == idx]
        print(f"\nCluster {idx}:")
        print(cluster_df[["Device_ID", "X", "Y"]].to_string(index=False))