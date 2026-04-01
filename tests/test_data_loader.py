import pandas as pd

from src.data_loader import carregar_dispositivos


def test_carregar_dispositivos_com_filtros(tmp_path):
    dados = pd.DataFrame({
        "Set": [1, 1, 2],
        "Subset": [1, 2, 1],
        "Device_ID": [0, 1, 2],
        "X": [10.0, 20.0, 30.0],
        "Y": [15.0, 25.0, 35.0]
    })

    arquivo_teste = tmp_path / "dispositivos_teste.csv"
    dados.to_csv(arquivo_teste, index=False)

    df, dispositivos = carregar_dispositivos(
        arquivo_teste,
        set_num=1,
        subset_num=2
    )

    assert len(df) == 1
    assert df.iloc[0]["Set"] == 1
    assert df.iloc[0]["Subset"] == 2
    assert dispositivos.shape == (1, 2)
    assert dispositivos[0][0] == 20.0
    assert dispositivos[0][1] == 25.0