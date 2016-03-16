$R_EXEC="& 'C:\Program Files\Microsoft\MRO\R-3.2.3\bin\Rscript.exe'"
$PYTHON_EXEC="D:\WinPython-64bit-3.5.1.2\python-3.5.1.amd64\python.exe"

# Download dos dados em python:

echo "Fazendo download das proposições votadas..."
Invoke-Expression "$PYTHON_EXEC src/python/obtem_proposicoes_votadas.py"

echo "Fazendo download da lista de deputados em exercicio atualmente..."
Invoke-Expression "$PYTHON_EXEC src/python/obtem_deputados_atual.py"

echo "Fazendo download das fotos dos deputados..."
Invoke-Expression "$PYTHON_EXEC src/python/download_fotos.py"

echo "Obtendo detalhes das proposições..."
Invoke-Expression "$PYTHON_EXEC src/python/obtem_detalhes_proposicoes.py"

echo "Obtendo votações das proposições..."
Invoke-Expression "$PYTHON_EXEC src/python/obtem_votacoes.py"

echo "Gerando séries temporais..."
Invoke-Expression "$PYTHON_EXEC src/python/gera_series_temporais.py"

# analise topologica em R:

echo "Calculando projeções..."
Invoke-Expression "$R_EXEC src/R/sliding-mds.R"

echo "Calculando topologias..."
Invoke-Expression "$R_EXEC src/R/gerar-topologias.R"

echo "Convertendo projeções para CSVs..."
Invoke-Expression "$R_EXEC src/R/converte-csv.R"
 
echo "Gerando arquivo com betti..."
Invoke-Expression "$R_EXEC src/R/gerar-betti.R"

echo "Gerando csv com betti e links para votações..."
Invoke-Expression "$R_EXEC src/R/gera-links-sliding.R"

echo "All done."
