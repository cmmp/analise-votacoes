#!/bin/bash

###############################################################
# Autor: Cassio M. M. Pereira <cassiomartini@gmail.com>
# Data: 16/03/2016 
# ############################################################
#
#
#           Configure o caminho dos dois executaveis:          
#
R_EXEC=/usr/bin/Rscript                                      
PYTHON_EXEC=/usr/bin/python3 # nao use python 2               
#
#         Nao se esqueca de alterar o workingdir no arquivo
#         src/params.json tambem!!!!
#
#
###############################################################

# Download dos dados em python:
echo "Fazendo download das proposicoes votadas..."
$PYTHON_EXEC src/python/obtem_proposicoes_votadas.py

echo "Fazendo download da lista de deputados em exercicio..."
$PYTHON_EXEC src/python/obtem_deputados_atual.py

echo "Fazendo download das fotos dos deputados... "
$PYTHON_EXEC src/python/download_fotos.py

echo "Obtendo detalhes das proposicoes..."
$PYTHON_EXEC src/python/obtem_detalhes_proposicoes.py

echo "Obtendo votacoes das proposicoes..."
$PYTHON_EXEC src/python/obtem_votacoes.py

echo "Gerando series temporais..."
$PYTHON_EXEC src/python/gera_series_temporais.py

# Analise topologica em R:
echo "Calculando projecoes..."
$R_EXEC src/R/sliding-mds.R

echo "Calculando topologias..."
$R_EXEC src/R/gerar-topologias.R

echo "Convertendo projecoes para CSV..."
$R_EXEC src/R/converte-csv.R

echo "Gerando arquivo com betti..."
$R_EXEC src/R/gerar-betti.R

echo "Gerando CSV com betti e links para votacoes..."
$R_EXEC src/R/gera-links-sliding.R

echo "All done..."

