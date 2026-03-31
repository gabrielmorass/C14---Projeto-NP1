import pandas as pd


def carregar_dispositivos(caminho_csv, set_num=None, subset_num=None):
    df = pd.read_csv(caminho_csv)

    if set_num is not None:
        df = df[df["Set"] == set_num]

    if subset_num is not None:
        df = df[df["Subset"] == subset_num]

    dispositivos = df[["X", "Y"]].values
    return df, dispositivos