# Trabalho Prático 1 - Equações Diferenciais Numéricas

## Visão Geral

Este repositório contém a implementação e análise de diversos métodos numéricos para a resolução de Problemas de Valor Inicial (PVIs) de Equações Diferenciais Ordinárias (EDOs). O projeto foi desenvolvido como parte do Trabalho Prático 1 da disciplina de Equações Diferenciais Numéricas da UFMG.

O objetivo principal é comparar o desempenho, a precisão e a ordem de convergência de métodos explícitos e implícitos em problemas lineares e não-lineares com soluções analíticas conhecidas.

## Métodos Implementados

Foram implementados os seguintes esquemas numéricos em Python, utilizando as bibliotecas NumPy e Matplotlib:

### Métodos Explícitos
* **Método de Euler** (Ordem 1)
* **Método de Heun** (Runge-Kutta de Ordem 2)
* **Método do Ponto Médio** (Runge-Kutta de Ordem 2)
* **Método de Runge-Kutta Clássico (RK4)** (Ordem 4)

### Métodos Implícitos
* **Método de Euler Regressivo** (Ordem 1)
* **Método do Trapézio** (Ordem 2)
* Estratégia de resolução para **problemas não-lineares** (solução de equação quadrática via Bhaskara para o Euler Regressivo).

## Estrutura do Projeto

O repositório está organizado da seguinte forma:
├── plots/              # Pasta onde os gráficos gerados são salvos
├── src/                # Pasta com todo o código-fonte
│   ├── methods.py      # Módulo com a implementação de todos os métodos numéricos
│   ├── main.py         # Script para comparar os métodos explícitos
│   ├── analise_ordem.py # Script para gerar a análise de ordem de convergência
│   ├── ...             # Outros scripts principais para os métodos implícitos
├── README.md           # Este arquivo
└── requirements.txt    # Lista de dependências Python do projeto

## Como Executar

### Pré-requisitos

* Python 3.x
* Git

### Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Mryan31/tp1_EDN.git](https://github.com/Mryan31/tp1_EDN.git)
    cd tp1_EDN
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Execução dos Scripts

Os principais scripts de análise podem ser executados a partir da pasta raiz do projeto:

* **Para gerar a análise de ordem dos métodos explícitos:**
    ```bash
    python src/analise_ordem.py
    ```

* **Para gerar a comparação dos métodos implícitos (linear):**
    ```bash
    python src/main_implicitos_linear.py
    ```

* **Para gerar a solução do problema não-linear:**
    ```bash
    python src/main_implicitos_naolinear.py
    ```

Os gráficos resultantes serão salvos na pasta `plots/`.

## Autor

* **Mateus Ryan de Castro Lima**