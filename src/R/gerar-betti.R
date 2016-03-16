require(jsonlite)
params  = fromJSON("src/params.json")
wd = params$workingdir
setwd(wd)

files = list.files(file.path(wd, "dados/diagrams"))

fnames = sort(as.numeric(gsub(".csv", "", files)))

BETTI = data.frame(id = numeric(0), dim0 = numeric(0), dim1 = numeric(0))

THRESHOLD = params$threshold

for (f in fnames) {
  D = read.csv(file.path(wd, "dados/diagrams", paste(f, ".csv", sep = '')))
  dim0 = nrow(D[D$dimension == 0,]) # we dont care about this as much
  mask = D$dimension == 1
  TTL = D[mask,3] - D[mask, 2]
  dim1 = sum(TTL >= THRESHOLD)
  BETTI = rbind(BETTI, data.frame(id = f, dim0 = dim0, dim1 = dim1))
}

write.csv(BETTI, file = file.path(wd, "dados/betti.csv"), row.names = F)
