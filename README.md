# Sprint 2 - Modelagem Linear para Aprendizado de Máquina - Challenge GoodWe: ChargeGrid Intelligence

## Integrantes

| Nome completo | RM |
| --- | --- |
| Davi Simoncelo | 571738 |
| Augusto de Souza Avila | 570839 |
| Murilo Lima de Carvalho | 570156 |
| João Pedro Sousa | 573962 |
| Matheus Evangelista | 568593 |

---

## 1. Introdução

Este relatório apresenta um estudo descritivo e analítico sobre sessões de recarga de veículos elétricos, desenvolvido a partir de uma base pública de dados de registros transacionais (*Electric Vehicle Charging Records*). O principal objetivo é mapear, caracterizar e interpretar os padrões de uso da infraestrutura de carregamento, traçando um paralelo estratégico com o ecossistema de soluções de recarga veicular e energia da GoodWe.

Para o desenvolvimento das análises, utilizou-se a linguagem de programação Python voltada à ciência de dados. A investigação estruturou-se em duas frentes fundamentais: uma análise gráfica detalhada explorando diferentes aspectos e tipologias das sessões, e uma análise univariada robusta focada em estatística descritiva para compreender o comportamento do consumo energético e o tempo de permanência dos usuários nos postos de carregamento. Os insights extraídos buscam apoiar diretamente decisões comerciais e operacionais que gerem valor sustentável para a companhia e seus parceiros.

---

## 2. Base de Dados

A base utilizada foi a **Electric Vehicle Charging Records**, publicada em conjunto com o artigo *"A dataset for multi-faceted analysis of electric vehicle charging transactions"*, da revista *Scientific Data*, e disponibilizada no Figshare sob licença CC BY 4.0.

O conjunto de dados reúne sessões de recarga realizadas em diferentes tipos de locais, como hotéis, empresas, apartamentos, restaurantes, resorts, instituições públicas e áreas públicas. A base tratada utilizada na análise está no arquivo `ChargingRecords` e possui **72.856 observações**.

Fonte consultada:
- Artigo: https://doi.org/10.1038/s41597-024-02942-9
- Base no Figshare: https://doi.org/10.6084/m9.figshare.22495141.v1

---

## 3. Análise Gráfica

A análise gráfica das variáveis foi conduzida utilizando as bibliotecas `matplotlib` e `seaborn` em Python, permitindo identificar características demográficas, estruturais e comportamentais da base de dados.

* **Distribuição dos Tipos de Carregadores:** Mostra a divisão da infraestrutura ativa. Observou-se que a grande maioria dos carregadores implantados corresponde a modelos convencionais ou lentos (*Slow Chargers*), totalizando **79,5%** das ocorrências, enquanto os carregadores rápidos (*Fast Chargers*) representam **20,5%** do ecossistema. Isso reforça que o hábito de recarga atual está massivamente associado a cenários onde o veículo permanece estacionado por períodos prolongados.
* **Quantidade de Sessões por Localização:** Evidencia quais locais geram maior volume transacional. Ambientes de uso público em geral (*public area*) e condomínios residenciais (*apartment*) lideram de forma expressiva o ranking, registrando mais de 14.000 sessões cada. Na sequência, destacam-se complexos de lazer e hotelaria (*resorts* e *hotels*) e ambientes corporativos (*companies*). Locais de conveniência rápida, como postos em garagens de ônibus ou pontos turísticos específicos, apresentam frequências residuais.
* **Distribuição da Demanda de Energia:** Os gráficos de distribuição revelam curvas de comportamento assimétrico à direita em ambas as variáveis principais (Demanda e Tempo de Recarga). A maior concentração de recargas de energia ocorre na base da escala (recargas rápidas/parciais), e a frequência de sessões decai gradualmente à medida que os valores de kWh e minutos aumentam, provando que sessões de consumo extremo e permanência ultralonga são menos usuais.
* **Gráfico de Distribuição do Tempo Total de Recarga:** O gráfico revela um comportamento de distribuição fortemente assimétrico à direita (assimetria positiva), onde a grande maioria das sessões de recarga se concentra em durações mais curtas. O pico mais expressivo do gráfico ocorre logo no início da escala temporal (na faixa aproximada de 20 a 60 minutos), o que indica que uma parcela massiva dos usuários utiliza a infraestrutura para cargas rápidas ou paradas breves de conveniência. À medida que o tempo avança para além das 2 horas (120 minutos), a curva sofre um declínio acentuado, estendendo-se em uma cauda longa e tênue que representa os casos isolados e menos frequentes de permanência ultralonga nas estações.

---

## 4. Análise Univariada e Estatística Descritiva

Esta seção aprofunda as propriedades numéricas das duas variáveis quantitativas fundamentais do estudo por meio das medidas de tendência central, dispersão e separatrizes.

### 4.1. Análise da Variável Demanda (kWh)

Foram calculadas as medidas de tendência central (média, mediana e moda), permitindo identificar o consumo energético típico das sessões de recarga. As medidas de dispersão (amplitude, variância, desvio-padrão e coeficiente de variação) possibilitaram avaliar a variabilidade do consumo entre os usuários. Já as medidas separatrizes (quartis e percentis) permitiram compreender a distribuição da demanda e identificar faixas de consumo mais frequentes.

* **Medidas de Tendência Central:**
  - **Média:** 17,44 kWh
  - **Mediana (Q2):** 14,10 kWh
  - **Moda:** 18,20 kWh

* **Medidas de Dispersão:**
  - **Mínimo:** 0,01 kWh | **Máximo:** 97,00 kWh
  - **Amplitude Total:** 96,99 kWh
  - **Variância:** 182,05 | **Desvio-padrão:** 13,49 kWh
  - **Coeficiente de Variação (CV):** 77,35%

* **Medidas Separatrizes:**
  - **Quartil 1 (Q1):** 7,53 kWh (25% das recargas consomem até este valor)
  - **Quartil 3 (Q3):** 23,20 kWh (75% das recargas consomem até este valor)
  - **Percentil 10 (P10):** 3,30 kWh | **Percentil 90 (P90):** 37,56 kWh

**Interpretação Estatística:** A demanda média por sessão gira em torno de 17,44 kWh, porém o Coeficiente de Variação de 77,35% aponta para uma alta dispersão dos dados. O consumo típico é moderado, visto que 90% de todas as sessões registradas no histórico demandam menos de 37,56 kWh (P90). A proximidade entre a mediana (14,10 kWh) e a moda (18,20 kWh) indica uma zona de consumo operacional padrão muito bem consolidada para veículos de passeio convencionais ou recargas diárias de manutenção.

### 4.2. Análise da Variável Tempo de Recarga (Minutos)

A análise do tempo de recarga permitiu identificar a duração típica das sessões por meio da média, mediana e moda. As medidas de dispersão mostraram o grau de heterogeneidade entre os tempos de carregamento observados. Os quartis e percentis auxiliaram na identificação dos intervalos que concentram a maior parte das sessões, fornecendo informações relevantes para o planejamento da utilização dos carregadores e da infraestrutura de recarga.

* **Medidas de Tendência Central:**
  - **Média:** 155,51 minutos (~2h35)
  - **Mediana (Q2):** 114,00 minutos (~1h54)
  - **Moda:** 40,00 minutos

* **Medidas de Dispersão:**
  - **Mínimo:** -29,00 minutos *(indica ruído/necessidade de saneamento na base original)*
  - **Máximo:** 4.717,00 minutos
  - **Amplitude Total:** 4.746,00 minutos
  - **Variância:** 25.339,38 | **Desvio-padrão:** 159,18 minutos
  - **Coeficiente de Variação (CV):** 102,37%

* **Medidas Separatrizes:**
  - **Quartil 1 (Q1):** 41,00 minutos
  - **Quartil 3 (Q3):** 204,00 minutos (~3h24)
  - **Percentil 10 (P10):** 21,00 minutos | **Percentil 90 (P90):** 360,00 minutos (6 hours)

**Interpretação Estatística:** O tempo de recarga é uma variável com volatilidade extrema (CV superior a 100%). Enquanto a moda se fixa em apenas 40 minutos (carregamentos rápidos ou paradas breves), a média é puxada para 155 minutos devido a sessões atípicas de longa permanência (veículos que passam a noite ou o horário comercial conectados). Metade dos usuários desocupa a vaga em até 114 minutos (Mediana), e 75% encerram a sessão em menos de 3 horas e 24 minutos (Q3), revelando a dinâmica de rotatividade das estações.

---

## 5. Tomada de Decisão e Geração de Valor para a GoodWe

A transformação dos registros descritivos e estatísticos em inteligência de negócios abre frentes fundamentais de atuação comercial e desenvolvimento tecnológico para a GoodWe:

1. **Otimização e Dimensionamento do Portfólio de Carregadores:** Sabendo que quase 80% das sessões ocorrem via carregadores lentos/semirrápidos e têm forte concentração em áreas públicas, condomínios e hotéis (onde a permanência do carro supera 2 horas), a GoodWe deve direcionar seus esforços comerciais de carregadores AC Inteligentes (linhas residenciais e comerciais de menor porte) para estes segmentos. Estações corporativas e condomínios comerciais demandam equipamentos com balanceamento dinâmico de carga (*Dynamic Load Management*), impedindo picos de queda na rede predial, dado que o desvio-padrão do consumo e do tempo é elevado.
2. **Gestão Inteligente da Energia (Integração com Solar e Baterias - EcoSmart Home):** Como a demanda de energia de 75% das sessões estabiliza-se abaixo de 23,20 kWh, a GoodWe pode empacotar comercialmente soluções combinadas "Inversor Solar + Bateria Estacionária + EV Charger". Uma bateria residencial ou comercial de pequeno/médio porte consegue suprir com folga a demanda integral da maioria das sessões mapeadas. Isso viabiliza o *peak shaving* (amortecimento de picos de consumo da rede distribuidora), utilizando a energia gerada pelos painéis solares durante o dia ou armazenada nas baterias para alimentar o carro sem sobrecarregar a infraestrutura local.
3. **Estratégias de Precificação e Gestão de Demanda Comercial:** A flutuação expressiva identificada no tempo de ocupação das vagas sinaliza a oportunidade de desenvolver softwares de gestão de carregamento com tarifas dinâmicas. Carregadores conectados a inversores híbridos GoodWe podem programar recargas automáticas nos horários de ociosidade da rede ou de pico de geração solar, gerando economia financeira real direta ao cliente final e maximizando o ROI dos ativos de energia.

---

## 6. Conclusão

A modelagem estatística descritiva aplicada à base transacional de recargas de veículos elétricos cumpre com sucesso o papel de converter dados brutos em direcionamento estratégico. A análise evidenciou duas realidades operacionais nítidas: a infraestrutura atual depende fortemente de carregamentos em locais de média a longa permanência (como áreas públicas, hotéis e residências), com demandas de energia concentradas predominantemente abaixo de 25 kWh por sessão.

Essas conclusões reforçam a tese de que o futuro da eletromobilidade está intrinsecamente conectado à descentralização energética. Para a GoodWe, os resultados chancelam a expansão e o aprimoramento de suas linhas de carregadores perfeitamente integrados aos sistemas de gerenciamento de baterias e inversores fotovoltaicos. Esta sinergia técnica não apenas soluciona os desafios operacionais de instabilidade na rede elétrica identificados nas distribuições de alta dispersão, mas também consolida o posicionamento de mercado da empresa como provedora líder de ecossistemas energéticos inteligentes, sustentáveis e de alto valor agregado.
