wd = "C://Users//Cássio//Dropbox//analise-votacoes//"
setwd(wd)

V = as.matrix(read.csv(file.path(wd, "series-votacoes-2015.csv")))
colnames(V) = NULL
cods = V[,1]

V = V[,2:ncol(V)] # remova id dos deputados
N = nrow(V)
C = matrix(0, nrow = N, ncol = N)

ptm = proc.time()
for(i in 1:(N-1)) {
  for(j in (i+1):(N)) {
    s = cor(V[i,], V[j,], method = 'spearman')
    C[i,j] = s
    C[j,i] = s
  }
}
proc.time() - ptm
diag(C) = 1

D = 1 - C # convert to a distance

save(C, file = 'spearman.RData')
save(D, file = 'distance.RData')


