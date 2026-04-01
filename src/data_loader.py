from pathlib import Path
import pandas as pd

from src.exceptions import DataFileError, DataValidationError


COLUNAS_OBRIGATORIAS = ["Set", "Subset", "Device_ID", "X", "Y"]


def carregar_dispositivos(caminho_csv, set_num=None, subset_num=None):
    caminho = Path(caminho_csv)


    # -----------------------------------
    #   TRATAMENTO DE ERROS
    #------------------------------------

    #Path errado
    if not caminho.exists():
        raise DataFileError(f"Arquivo não encontrado: {caminho_csv}")

    #Não é CSV
    if caminho.suffix.lower() != ".csv":
        raise DataFileError("O arquivo deve ser um CSV.")

    #Leitura
    try:
        df = pd.read_csv(caminho)
    except pd.errors.EmptyDataError:
        raise DataValidationError("CSV vazio.")
    except Exception as e:
        raise DataFileError(f"Erro ao ler o CSV: {e}")

    # CSV vazio
    if df.empty:
        raise DataValidationError("CSV não contém dados.")

    #Colunas faltando
    colunas_faltando = [c for c in COLUNAS_OBRIGATORIAS if c not in df.columns]
    if colunas_faltando:
        raise DataValidationError(f"Colunas ausentes: {colunas_faltando}")

    #Filtros
    if set_num is not None:
        df = df[df["Set"] == set_num]

    if subset_num is not None:
        df = df[df["Subset"] == subset_num]

    #Caso o filtro nao retorne nada
    if df.empty:
        raise DataValidationError("Nenhum dado encontrado após filtro.")

    #Valor nulo
    if df[["X", "Y"]].isnull().any().any():
        raise DataValidationError("Valores nulos encontrados.")

    #Valor não numérico
    try:
        df["X"] = pd.to_numeric(df["X"])
        df["Y"] = pd.to_numeric(df["Y"])
    except Exception:
        raise DataValidationError("Valores não numéricos em X ou Y.")

    dispositivos = df[["X", "Y"]].values

    return df, dispositivos