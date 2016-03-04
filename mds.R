wd = "C://Users//Cássio//Dropbox//analise-votacoes//"
setwd(wd)

load("distance.RData")

V = as.matrix(read.csv(file.path(wd, "series-votacoes-2015.csv")))
colnames(V) = NULL
cods = V[,1]
rm(V)

DEP = read.csv(file.path(wd, "deputados.csv"))
partidos = DEP[DEP$ideCadastro %in% cods,10]

base = c('PT', 'PCdoB', 'PMDB', 'PDT', 'PSDC', 'PROS', 'PP', 'PSD')
estaNaBase = partidos %in% base

M = cmdscale(D, k = 2)

plot(M, col = estaNaBase + 1)
