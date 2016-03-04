# Análise de votações

Este código faz uma análise das votações na camâmara dos deputados durante um ano em particular.

A idéia é analisar como a topologia dos dados varia ao longo do tempo.

Para realizar a análise, séries temporais das votações são geradas, considerando os seguintes valores:

* Valor  1: voto sim
* Valor -1: voto não
* Valor  0: abstenção ou ausência do voto

Para gerar pontos no espaço a partir das séries temporais, calcula-se a correlação de [Spearman](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient), a qual é convertida para uma distância usando a equação `D = 1 - S`. Os pontos são gerados por meio da execução de [Multidimensional Scaling](https://en.wikipedia.org/wiki/Multidimensional_scaling).


