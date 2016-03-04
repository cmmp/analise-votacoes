wd = "C://Users//Cássio//Dropbox//analise-votacoes//"
setwd(wd)

calcularDist = function(S) {
  # S e uma matriz com uma serie temporal por linha
  
  
}

V = as.matrix(read.csv(file.path(wd, "series-votacoes-2015.csv")))
colnames(V) = NULL
cods = V[,1]

V = V[,2:ncol(V)] # remova id dos deputados
N = nrow(V)
C = matrix(0, nrow = N, ncol = N)


