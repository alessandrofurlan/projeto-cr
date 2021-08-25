# Projeto WFABCaze

## Objetivo

O WFABCaze foi o projeto final da disciplina de Comunicação de Redes do segundo quadrimestre de 2020 e teve como objetivo a modelagem e o desenvolvimento de um algoritmo de GPS para o campus de São Bernardo do Campo da UFABC.


## Modelagem

A modelagem do campus foi feita, primeiramente, pela definição de pontos de interesse no mapa e nas plantas base do campus.

<p align="center">
  <img src=https://github.com/alessandrofurlan/projeto-cr/blob/master/images/vertices_sbc.png>
</p>
<p align="center">
  <i> Pontos de interesse da parte de transferência do campus de SBC </i>
</p>

Além da parte de transferência, foram modelados, também, os blocos Alpha 1 e Alpha 2, que possuem 4 andares cada.
Com esses pontos, foi definido as arestas e suas distâncias, as quais foram calculadas por meio da escala junto ao programa <em>Inkscape</em>. E, por algoritmos encontrados nos arquivos parse_svg_alfa1.ipynb e parse_svg_alfa2.ipynb, foram obtidos arquivos .csv que puderam ser transformados em grafos com ajuda da biblioteca <em>NetworkX</em>.

## Algoritmo de GPS

O algoritmo de um GPS se baseia, essencialmente, em duas funções, que foram o objetivo desse projeto: a função de caminho mais curto (<em>shortest path</em>) e a de distância de um caminho.
A partir dos gráfos, foi feito um algoritmo capaz de realizar essas duas funções entre dois vértices levando em consideração a distância de cada aresta.

## Discussão dos Grafos

O gráfo do campus obtido a partir da biblioteca <em>iGraph</em> foi o seguinte:

<p align="center">
  <img src=https://github.com/alessandrofurlan/projeto-cr/blob/master/images/grafo_igraph.png>
</p>
<p align="center">
  <i> Gráfo do campus de SBC </i>
</p>

E sua distribuição de comunidades, pela mesma biblioteca foi:

<p align="center">
  <img src=https://github.com/alessandrofurlan/projeto-cr/blob/master/images/comunidades_igraph_com_labels.png>
</p>
<p align="center">
  <i> Pontos de interesse da parte exterior do campus de SBC </i>
</p>

 O método utilizado retornou comunidades plausíveis, as quais correspondem de forma parcial às comunidades esperadas, que seriam, por exemplo, os andares dos blocos e a parte de transferência. Obteve-se comunidades com salas de andares diferentes misturadas, mas ainda sim, foram retornadas 4 comunidades para cada bloco e uma para a parte de transferência, o que condiz com os 4 andares de cada bloco.
