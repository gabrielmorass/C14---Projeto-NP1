# Optimizing Power Beacon Placement using K-means

## 📌 Descrição

Este projeto tem como objetivo determinar o posicionamento ideal de *power beacons* com base na distribuição espacial de dispositivos, utilizando o algoritmo de clusterização K-means.

Os dispositivos são representados por coordenadas (X, Y), e os centroides dos clusters são utilizados como posições ótimas para os beacons.

---

## 🎯 Objetivo

Desenvolver um sistema com pipeline completo de CI/CD que:

* Realiza clusterização de dispositivos
* Determina posições ideais para power beacons
* Garante qualidade através de testes automatizados
* Automatiza build, testes e deploy

---

## 🛠️ Tecnologias

* Python 3.11
* Pandas
* NumPy
* Scikit-learn (K-means)
* Matplotlib
* FastAPI
* Pytest
* GitHub Actions (CI/CD)

---

## ⚙️ Instalação

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ▶️ Como executar

```bash
python src/main.py
```

---

## 🧪 Testes

Executar testes com:

```bash
pytest
```

