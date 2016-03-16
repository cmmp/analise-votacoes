require(jsonlite)
params  = fromJSON("src/params.json")
wd = params$workingdir
setwd(wd)

V = read.csv(file.path(wd, "dados/series-votacoes-2015.csv"))
cods = V[,1]
V = V[,2:ncol(V)] # remova id dos deputados

P = read.csv(file.path(wd, "dados/detalhes-props-2015.csv"))

votes = colnames(V)
votes = gsub("X", "", votes)
votes = strsplit(votes, ".", fixed = TRUE)
votes = as.numeric(sapply(votes, function(x) x[1])) # extract only the ids

W = params$W
slide = params$slide
m = ncol(V)
#k = 1
Nw = floor((m-W)/slide + 1)

INFO = data.frame(propostas = character(0), links = character(0))

for(i in seq(1, m - W + 1, by = slide)) { # |_(m-W)/slide + 1_|
  #cat("Processando a janela k =", k, "/", Nw, "\n")
  idxs = i:(i + W - 1)
  mask = P$idProposicao %in% votes[idxs]
  toAdd = data.frame(#janela = k, 
                     propostas = paste(P[mask,4],collapse=";"), 
                     links = paste(P[mask,15],collapse=";")
  )
  INFO = rbind(INFO, toAdd)
 # k = k + 1
}

BETTIORIG = read.csv(file.path(wd, "dados/betti.csv"))

write.csv(cbind(BETTIORIG, INFO), file = file.path(wd, "dados/betti-info.csv"), fileEncoding = 'UTF-8', row.names = F)
