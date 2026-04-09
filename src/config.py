from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_CSV = BASE_DIR / "data" / "dispositivos_30x30_uniforme.csv"

N_CLUSTERS = 4
SET_ESCOLHIDO = 10
SUBSET_ESCOLHIDO = 5

X_LIM = (0, 30)
Y_LIM = (0, 30)

RANDOM_STATE = 42
N_INIT = 10