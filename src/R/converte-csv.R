# converte rdata para csv:

require(jsonlite)
params  = fromJSON("src/params.json")
wd = params$workingdir
setwd(wd)

files = list.files(file.path(wd, "dados/projecoes"))

V = as.matrix(read.csv(file.path(wd, "dados/series-votacoes-2015.csv")))
colnames(V) = NULL
cods = V[,1]
rm(V)

DEP = read.csv(file.path(wd, "dados/deputados.csv"))
partidos = DEP[DEP$ideCadastro %in% cods,10]

base = c('PT', 'PCdoB', 'PMDB', 'PDT', 'PSDC', 'PROS', 'PP', 'PSD')
estaNaBase = partidos %in% base
estaNaBase = ifelse(estaNaBase, "Base", "Oposicao")

mask = DEP$ideCadastro %in% cods

if(!file.exists(file.path(wd, "dados/csv"))) {
  dir.create(file.path(wd, "dados/csv"))
}

i = 1
for (f in files) {
  load(file.path(wd, "dados/projecoes", f))
  write.table(cbind(as.data.frame(P),estaNaBase,DEP[mask,'ideCadastro'],DEP[mask,'nomeParlamentar'],DEP[mask,'partido']), 
              file = file.path(wd, "dados/csv", paste(i,".csv",sep='')), 
              quote=F,col.names=c("x1","x2","classe", "ideDeputado", "nome", "partido"),
                                  fileEncoding = 'UTF-8',
              sep = ',',row.names=F)
  i = i + 1
}
