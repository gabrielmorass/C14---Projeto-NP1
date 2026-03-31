def imprimir_dispositivos_por_cluster(df, labels, n_clusters):
    df_resultado = df.copy()
    df_resultado["Cluster"] = labels

    for idx in range(n_clusters):
        cluster_df = df_resultado[df_resultado["Cluster"] == idx]
        print(f"\nCluster {idx + 1}:")
        print(cluster_df[["Device_ID", "X", "Y"]].to_string(index=False))