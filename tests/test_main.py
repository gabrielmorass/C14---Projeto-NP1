import runpy
import numpy as np
from unittest.mock import patch


@patch("data_loader.carregar_dispositivos")
@patch("clustering.aplicar_kmeans")
@patch("plotting.plotar_clusters")
@patch("reporting.imprimir_dispositivos_por_cluster")
def test_main_fluxo(
    mock_report,
    mock_plot,
    mock_kmeans,
    mock_loader
):
    # 🔹 Mock dos retornos
    mock_loader.return_value = ("df_fake", [[1, 2], [3, 4]])
    mock_kmeans.return_value = (
        np.array([0, 1]),
        np.array([[1, 2], [3, 4]])
    )

    # 🔥 Executa a main como script
    runpy.run_module("main", run_name="__main__")

    # 🔹 Verifica chamadas
    mock_loader.assert_called_once()
    mock_kmeans.assert_called_once()
    mock_plot.assert_called_once()
    mock_report.assert_called_once()