import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

from src.plotting import plotar_clusters
from src.config import X_LIM, Y_LIM


def test_plotar_clusters_executa_sem_erro(monkeypatch):
    chamado = {"show": False}

    def fake_show():
        chamado["show"] = True

    monkeypatch.setattr(plt, "show", fake_show)

    dispositivos = np.array([
        [1, 1],
        [2, 2],
        [8, 8],
        [9, 9],
    ])
    labels = np.array([0, 0, 1, 1])
    centros = np.array([
        [1.5, 1.5],
        [8.5, 8.5],
    ])

    plotar_clusters(dispositivos, labels, centros, n_clusters=2, titulo="Teste")

    assert chamado["show"] is True


def test_plotar_clusters_define_limites_corretos(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    dispositivos = np.array([
        [1, 1],
        [2, 2],
        [8, 8],
        [9, 9],
    ])
    labels = np.array([0, 0, 1, 1])
    centros = np.array([
        [1.5, 1.5],
        [8.5, 8.5],
    ])

    plotar_clusters(dispositivos, labels, centros, n_clusters=2)

    ax = plt.gca()
    assert tuple(ax.get_xlim()) == X_LIM
    assert tuple(ax.get_ylim()) == Y_LIM


def test_plotar_clusters_define_titulo(monkeypatch):
    monkeypatch.setattr(plt, "show", lambda: None)

    dispositivos = np.array([
        [1, 1],
        [2, 2],
        [8, 8],
        [9, 9],
    ])
    labels = np.array([0, 0, 1, 1])
    centros = np.array([
        [1.5, 1.5],
        [8.5, 8.5],
    ])

    titulo = "Meu Grafico de Teste"
    plotar_clusters(dispositivos, labels, centros, n_clusters=2, titulo=titulo)

    ax = plt.gca()
    assert ax.get_title() == titulo