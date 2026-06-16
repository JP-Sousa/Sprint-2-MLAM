# -*- coding: utf-8 -*-
"""Sprint 2 MLAM.py"""

import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# CONFIGURAÇÕES
# =====================================================

ARQUIVO_DADOS = "ChargingRecords.csv"

# =====================================================
# FUNÇÕES DE TRATAMENTO DE DADOS
# =====================================================

def carregar_dados(caminho):
    """
    Carrega a base de dados e realiza as conversões necessárias.

    Parâmetros:
        caminho (str): Caminho do arquivo CSV.

    Retorno:
        pd.DataFrame: Base de dados tratada.
    """
    dados = pd.read_csv(caminho)

    dados["StartDatetime"] = pd.to_datetime(dados["StartDatetime"])
    dados["EndDatetime"] = pd.to_datetime(dados["EndDatetime"])

    # Hora de início da sessão
    dados["HoraInicio"] = dados["StartDatetime"].dt.hour

    # Tempo total de recarga em minutos
    dados["TempoRecargaMin"] = (
        dados["EndDatetime"] - dados["StartDatetime"]
    ).dt.total_seconds() / 60

    return dados


# =====================================================
# FUNÇÕES DE ANÁLISE GRÁFICA ESPECÍFICA
# =====================================================

def grafico_setores(dados):
    """
    Exibe um gráfico de setores com a distribuição dos tipos de carregadores.
    """
    tipos = dados["ChargerType"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        tipos,
        labels=tipos.index,
        autopct="%1.1f%%",
        colors=plt.cm.Set3.colors
    )

    plt.title("Distribuição dos Tipos de Carregadores")

    plt.legend(
        ["Slow Charger", "Fast Charger"],
        title="Tipos de Carregador",
        loc="best"
    )

    plt.show()


def grafico_barras(dados):
    """
    Exibe um gráfico de barras com a quantidade de sessões por localização.
    """
    localizacoes = dados["Location"].value_counts()

    plt.figure(figsize=(10, 6))

    plt.bar(
        localizacoes.index,
        localizacoes.values,
        color="steelblue",
        label="Quantidade de Sessões"
    )

    plt.title("Quantidade de Sessões por Localização")
    plt.xlabel("Localização")
    plt.ylabel("Quantidade de Sessões")

    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def histograma_demanda(dados):
    """
    Exibe a distribuição da demanda de energia.
    """
    plt.figure(figsize=(10, 6))

    plt.hist(
        dados["Demand"].dropna(),
        bins=20,
        color="tomato",
        edgecolor="black"
    )

    plt.title("Distribuição da Demanda de Energia")
    plt.xlabel("Demanda de Energia (kWh)")
    plt.ylabel("Frequência")

    plt.tight_layout()
    plt.show()


def histograma_tempo_recarga(dados):
    """
    Exibe a distribuição do tempo total de recarga.
    """
    tempo_recarga = dados["TempoRecargaMin"].dropna()

    plt.figure(figsize=(10, 6))

    plt.hist(
        tempo_recarga,
        bins=30,
        range=(0, 1500),
        color="orange",
        edgecolor="black"
    )

    plt.xlim(0, 1500)
    plt.xticks(range(0, 1501, 150))

    plt.title("Distribuição do Tempo Total de Recarga")
    plt.xlabel("Tempo de Recarga (minutos)")
    plt.ylabel("Frequência")

    plt.tight_layout()
    plt.show()


def boxplot_tempo_recarga(dados):
    """
    Exibe um boxplot horizontal do tempo total de recarga.
    Os outliers são ocultados para melhorar a visualização.
    """
    tempo_recarga = dados["TempoRecargaMin"].dropna()

    limite_superior = tempo_recarga.quantile(0.95)

    plt.figure(figsize=(12, 3))

    # Correção do aviso MatplotlibDeprecationWarning: alterado 'vert=False' para 'orientation="horizontal"'
    plt.boxplot(
        tempo_recarga,
        orientation="horizontal",
        showfliers=False,
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen")
    )

    plt.xlim(0, limite_superior)

    plt.title("Boxplot do Tempo Total de Recarga")
    plt.xlabel("Tempo de Recarga (minutos)")
    plt.ylabel("Sessões de Recarga")

    plt.tight_layout()
    plt.show()


# =====================================================
# FUNÇÃO DE ANÁLISE ESTATÍSTICA UNIVARIADA
# =====================================================

def analise_univariada(serie, nome_variavel, unidade=""):
    """
    Realiza análise estatística e gera gráficos para uma variável específica.
    """

    print("\n" + "=" * 60)
    print(f"ANÁLISE UNIVARIADA - {nome_variavel.upper()}")
    print("=" * 60)

    # =====================================================
    # TENDÊNCIA CENTRAL
    # =====================================================

    media = serie.mean()
    mediana = serie.median()
    moda = serie.mode()

    print("\nMEDIDAS DE TENDÊNCIA CENTRAL")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")

    if len(moda) > 0:
        print(f"Moda: {moda.iloc[0]:.2f}")

    # =====================================================
    # DISPERSÃO
    # =====================================================

    minimo = serie.min()
    maximo = serie.max()
    amplitude = maximo - minimo
    variancia = serie.var()
    desvio_padrao = serie.std()
    coef_variacao = (desvio_padrao / media) * 100 if media != 0 else 0

    print("\nMEDIDAS DE DISPERSÃO")
    print(f"Mínimo: {minimo:.2f}")
    print(f"Máximo: {maximo:.2f}")
    print(f"Amplitude: {amplitude:.2f}")
    print(f"Variância: {variancia:.2f}")
    print(f"Desvio-padrão: {desvio_padrao:.2f}")
    print(f"Coeficiente de Variação: {coef_variacao:.2f}%")

    # =====================================================
    # SEPARATRIZES
    # =====================================================

    q1 = serie.quantile(0.25)
    q2 = serie.quantile(0.50)
    q3 = serie.quantile(0.75)

    p10 = serie.quantile(0.10)
    p90 = serie.quantile(0.90)

    print("\nMEDIDAS SEPARATRIZES")
    print(f"Q1: {q1:.2f}")
    print(f"Q2 (Mediana): {q2:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"P10: {p10:.2f}")
    print(f"P90: {p90:.2f}")

    # =====================================================
    # HISTOGRAMA
    # =====================================================

    limite = serie.quantile(0.95)

    plt.figure(figsize=(10, 5))

    plt.hist(
        serie[serie <= limite],
        bins=20,
        color="steelblue",
        edgecolor="black"
    )

    plt.axvline(
        media,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Média = {media:.2f}"
    )

    plt.axvline(
        mediana,
        color="green",
        linestyle="-.",
        linewidth=2,
        label=f"Mediana = {mediana:.2f}"
    )

    plt.title(f"Histograma - {nome_variavel}")
    plt.xlabel(f"{nome_variavel} ({unidade})")
    plt.ylabel("Frequência")

    plt.xlim(0, limite)

    plt.legend()
    plt.tight_layout()
    plt.show()

    # =====================================================
    # BOXPLOT
    # =====================================================

    plt.figure(figsize=(5, 7))

    plt.boxplot(
        serie,
        patch_artist=True,
        showfliers=False,
        showmeans=True,
        boxprops=dict(facecolor="lightgreen")
    )

    plt.ylim(0, limite)

    plt.title(f"Boxplot - {nome_variavel}")
    plt.ylabel(f"{nome_variavel} ({unidade})")

    plt.tight_layout()
    plt.show()


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

def main():
    """
    Executa todas as análises gráficas e estatísticas de forma sequencial.
    """
    # Carrega o dataframe de forma local
    dados = carregar_dados(ARQUIVO_DADOS)

    # 1. Gráficos Gerais
    grafico_setores(dados)
    grafico_barras(dados)
    histograma_demanda(dados)
    histograma_tempo_recarga(dados)
    boxplot_tempo_recarga(dados)

    # 2. Análise Univariada da Demanda (Correção do NameError: puxando o dataframe local)
    analise_univariada(
        dados["Demand"].dropna(),
        "Demanda",
        "kWh"
    )

    # 3. Análise Univariada do Tempo de Recarga
    analise_univariada(
        dados["TempoRecargaMin"].dropna(),
        "Tempo de Recarga",
        "min"
    )


if __name__ == "__main__":
    main()