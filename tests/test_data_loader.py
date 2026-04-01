from pathlib import Path
import pandas as pd
import pytest

from src.data_loader import carregar_dispositivos
from src.exceptions import DataFileError, DataValidationError


BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_PATH = BASE_DIR / "data" / "dispositivos_30x30_uniforme.csv"


def test_carregar_dataset_real():
    df, dispositivos = carregar_dispositivos(DATASET_PATH)

    assert not df.empty
    assert dispositivos.shape[1] == 2


def test_carregar_com_filtro_real():
    df, dispositivos = carregar_dispositivos(
        DATASET_PATH,
        set_num=10,
        subset_num=5
    )

    assert not df.empty
    assert all(df["Set"] == 10)
    assert all(df["Subset"] == 5)


def test_arquivo_inexistente():
    with pytest.raises(DataFileError):
        carregar_dispositivos("arquivo_inexistente.csv")


def test_csv_vazio(tmp_path):
    arquivo = tmp_path / "vazio.csv"
    pd.DataFrame().to_csv(arquivo, index=False)

    with pytest.raises(DataValidationError):
        carregar_dispositivos(arquivo)


def test_colunas_ausentes(tmp_path):
    dados = pd.DataFrame({
        "A": [1],
        "B": [2]
    })

    arquivo = tmp_path / "dados.csv"
    dados.to_csv(arquivo, index=False)

    with pytest.raises(DataValidationError):
        carregar_dispositivos(arquivo)


def test_filtro_sem_resultado(tmp_path):
    dados = pd.DataFrame({
        "Set": [1],
        "Subset": [1],
        "Device_ID": [0],
        "X": [10],
        "Y": [10]
    })

    arquivo = tmp_path / "dados.csv"
    dados.to_csv(arquivo, index=False)

    with pytest.raises(DataValidationError):
        carregar_dispositivos(arquivo, set_num=999)


def test_valores_nao_numericos(tmp_path):
    dados = pd.DataFrame({
        "Set": [1],
        "Subset": [1],
        "Device_ID": [0],
        "X": ["a"],
        "Y": ["b"]
    })

    arquivo = tmp_path / "dados.csv"
    dados.to_csv(arquivo, index=False)

    with pytest.raises(DataValidationError):
        carregar_dispositivos(arquivo)


def test_valores_nulos(tmp_path):
    dados = pd.DataFrame({
        "Set": [1],
        "Subset": [1],
        "Device_ID": [0],
        "X": [None],
        "Y": [10]
    })

    arquivo = tmp_path / "dados.csv"
    dados.to_csv(arquivo, index=False)

    with pytest.raises(DataValidationError):
        carregar_dispositivos(arquivo)