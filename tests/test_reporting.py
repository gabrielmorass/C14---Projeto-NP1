import pandas as pd
import numpy as np

from reporting import imprimir_dispositivos_por_cluster



def gerar_dataframe():
    df = pd.DataFrame({
        "Device_ID": [1, 2, 3, 4],
        "X": [1, 1, 10, 10],
        "Y": [2, 3, 10, 11]
    })

    labels = np.array([0, 0, 1, 1])

    return df, labels


#  Teste 1: verifica se imprime clusters corretamente
def test_saida_clusters(capsys):
    df, labels = gerar_dataframe()

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    captured = capsys.readouterr()
    output = captured.out

  
    assert "Cluster 1" in output
    assert "Cluster 2" in output

  
    assert "1" in output
    assert "4" in output


#  Teste 2: número de clusters impressos
def test_numero_clusters(capsys):
    df, labels = gerar_dataframe()

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    output = capsys.readouterr().out

  
    assert output.count("Cluster") == 2


#  Teste 3: não altera dataframe original
def test_dataframe_nao_modificado():
    df, labels = gerar_dataframe()

    df_original = df.copy()

    imprimir_dispositivos_por_cluster(df, labels, n_clusters=2)

    # verifica se o df original não foi alterado
    assert "Cluster" not in df.columns
    assert df.equals(df_original)
