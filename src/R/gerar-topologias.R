require(TDA)
require(jsonlite)

params  = fromJSON("src/params.json")
wd = params$workingdir
setwd(wd)

set.seed(1234)

datadir = file.path(wd, "dados/projecoes")

projs = list.files(datadir)
basenames = gsub(".RData", "", projs)
basenames = sort(as.numeric(basenames))

if(!file.exists(file.path(wd, "dados/diagrams"))) {
  dir.create(file.path(wd, "dados/diagrams"))
}

maxdimension = 1 # max d of simplices: 0 connected comp; 1 loops; 2 voids...

i = 1
for (bname in basenames) {
  cat(date(), "-- Processing file", bname, "\n")
  load(file.path(datadir, paste(bname, ".RData", sep='')))

  D = dist(P)
  maxscale = max(D)
  
  Diag = ripsDiag(P, maxdimension = maxdimension, maxscale = maxscale, dist = "euclidean", library = "GUDHI")$diagram
  write.csv(Diag, file = file.path(wd, "dados/diagrams", paste(basenames[i], ".csv", sep = '')), row.names = F)
  t = as.matrix(table(Diag[,1]))
  
  i = i + 1
}

