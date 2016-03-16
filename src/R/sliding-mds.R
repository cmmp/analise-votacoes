require(jsonlite)
params  = fromJSON("src/params.json")
wd = params$workingdir
setwd(wd)

calcularDist = function(S) {
  # S e uma matriz com uma serie temporal por linha
  N = nrow(S)
  C = matrix(0, nrow = N, ncol = N)
  ptm = proc.time()
  for(i in 1:(N-1)) {
    for(j in (i+1):(N)) {
      s = cor(S[i,], S[j,], method = 'spearman')
      C[i,j] = s
      C[j,i] = s
    }
  }
  proc.time() - ptm
  diag(C) = 1
  C[is.na(C)] = 0 # necessario pq algumas series podem ser constantes dentro da janela...
  
  D = 1 - C # convert to a distance
  return(D)
}

calcularProjecao = function(S) {
  D = calcularDist(S)
  P = cmdscale(D, k = 2)
  return(P)
}

V = as.matrix(read.csv(file.path(wd, "dados/series-votacoes-2015.csv")))
colnames(V) = NULL
cods = V[,1]
V = V[,2:ncol(V)] # remova id dos deputados

# calcule as projecoes usando uma sliding window
# sobre as series de votacoes
W = params$W
slide = params$slide
m = ncol(V)
k = 1
Nw = floor((m-W)/slide + 1)

if(!file.exists(file.path(wd, "dados/projecoes"))) {
  dir.create(file.path(wd, "dados/projecoes"))
}

for(i in seq(1, m - W + 1, by = slide)) { # |_(m-W)/slide + 1_|
  cat("Processando a janela k =", k, "/", Nw, "\n")
  S = V[,i:(i + W - 1)]
  P = calcularProjecao(S)
  save(P, file = file.path(wd, "dados/projecoes", paste(k, ".RData", sep = '')))
  k = k + 1
}
