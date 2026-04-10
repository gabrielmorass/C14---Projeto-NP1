# Optimizing Power Beacon Placement using K-means

[![CI](https://github.com/gabrielmorass/C14---Projeto-NP1/actions/workflows/ci.yml/badge.svg)](https://github.com/gabrielmorass/C14---Projeto-NP1/actions/workflows/ci.yml)
[![Deploy Results](https://github.com/gabrielmorass/C14---Projeto-NP1/actions/workflows/deploy-results.yml/badge.svg)](https://github.com/gabrielmorass/C14---Projeto-NP1/actions/workflows/deploy-results.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Online-success)](https://gabrielmorass.github.io/C14---Projeto-NP1/)

## Descrição

Este projeto tem como objetivo determinar o posicionamento ideal de **power beacons** com base na distribuição espacial de dispositivos, utilizando o algoritmo de clusterização **K-means**.

Os dispositivos são representados por coordenadas **(X, Y)**, e os centroides dos clusters são utilizados como posições ótimas para os beacons.

Além da modelagem e visualização dos resultados, o projeto conta com pipeline de **CI/CD**, testes automatizados e **deploy automático dos resultados** com **GitHub Pages**.

---

## Objetivo

Desenvolver um sistema com pipeline completo que:

- realiza a clusterização de dispositivos;
- determina posições ideais para power beacons;
- gera visualizações e relatórios automaticamente;
- garante qualidade com testes automatizados;
- publica os resultados automaticamente com GitHub Actions e GitHub Pages.

---

## Tecnologias utilizadas

- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- FastAPI
- Uvicorn
- Pytest
- Pytest-cov
- GitHub Actions
- GitHub Pages

---

## Estrutura do projeto

```text
C14---Projeto-NP1/
├── .github/workflows/     # Workflows de CI, build e deploy
├── data/                  # Dataset utilizado pelo projeto
├── results/               # Resultados gerados automaticamente
├── src/                   # Código-fonte principal
├── tests/                 # Testes automatizados
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Instalação

### Clonar o repositório e configurar o ambiente

#### Windows

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

#### Linux/macOS

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Como rodar o projeto

### Execução simples

```bash
python -m src.main
```

### Fluxo completo no Windows

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.main
```

### Fluxo completo no Linux/macOS

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
```

A execução gera automaticamente os arquivos de saída na pasta `results/`, incluindo:

- `clusters.png`
- `cluster_report.csv`

---

## Como rodar os testes

### Execução simples

```bash
pytest -v
```

### Fluxo completo no Windows

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

### Fluxo completo no Linux/macOS

```bash
git clone https://github.com/gabrielmorass/C14---Projeto-NP1.git
cd C14---Projeto-NP1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

---

## Integração contínua

O projeto utiliza GitHub Actions para automatizar:

- execução dos testes unitários;
- empacotamento do projeto;
- geração e publicação dos resultados.

Os workflows configurados no repositório são:

- **CI**: executa testes e build;
- **Deploy Results**: gera os resultados e publica no GitHub Pages.

---

## Deploy dos resultados

Sempre que há atualização na branch `main`, o workflow de deploy:

1. instala as dependências do projeto;
2. executa o código principal;
3. gera os arquivos de resultado;
4. monta uma página HTML automática;
5. publica os artefatos no GitHub Pages.

Os resultados publicados incluem:

- visualização da clusterização;
- relatório CSV para download.

---

## Acesso aos resultados

Os resultados publicados podem ser acessados diretamente no link abaixo:

[🔗 Abrir site com os resultados](https://gabrielmorass.github.io/C14---Projeto-NP1/)

---

## Resultados gerados

Os principais artifacts gerados pelo projeto são:

- `results/clusters.png`
- `results/cluster_report.csv`

Esses arquivos também são utilizados no processo de deploy automático.
