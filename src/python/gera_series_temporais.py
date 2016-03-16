# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:47:42 2016

@author: Cássio
"""

import os
import csv
from datetime import datetime


exec(open("src/python/load_params.py").read())

basepath = wd + 'dados/' + str(ano) + '/votacoes/'

codigos = [] # codigos das proposicoes
datas   = [] # datas das votacoes

with open(wd + "dados/votadas-" + str(ano) + ".csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        codigos.append(row['codProposicao'])

last = ''
for cod in codigos:
    if cod != last:
        datasEhoras = os.listdir(basepath + cod)
        datasEhoras = [x.replace(".csv", "") for x in datasEhoras]
        datasEhoras = [datetime.strptime(x, "%d-%m-%Y--%H-%M") for x in datasEhoras]
        datas.extend(datasEhoras)
        last = cod


# reordene as proposicoes e datas para que fiquem em ordem temporal
# segundo as datas de votacoes
srtidx  = sorted(range(len(datas)), key = lambda x : datas[x])
datas   = [datas[i] for i in srtidx]
codigos = [codigos[i] for i in srtidx]


# salvamos no formato idProposicao-dataVotacao-hora, 
# sendo a serie temporal ordenada pelas datas das votacoes
fieldnames = ['idDeputado']
for i in range(len(datas)):
    fieldnames.append(codigos[i] + "-" + datetime.strftime(datas[i], "%d-%m-%Y-%H-%M"))

escapechar = '\\'

with open(wd + "dados/series-votacoes-" + str(ano) + ".csv", 'w') as outfile:
    writer = csv.writer(outfile,
                            lineterminator = '\n', 
                            quoting = csv.QUOTE_NONNUMERIC, 
                            escapechar = escapechar)
    writer.writerow(fieldnames)
    # leia a lista de deputados atuais:
    with open(wd + "dados/deputados.csv", 'r') as depfile:
        reader = csv.DictReader(depfile)        
        for row in reader:
            depNome = row['nomeParlamentar'].upper()
            votos = [row['ideCadastro']]
            print("Processando parlamentar", depNome)
            # leia todas as votacoes deste deputado            
            zeroCount = 0
            for i in range(len(datas)):
                dia    = datetime.strftime(datas[i], "%d").lstrip('0')
                mes    = datetime.strftime(datas[i], "%m").lstrip('0')
                ano    = datetime.strftime(datas[i], "%Y")
                hora   = datetime.strftime(datas[i], "%H")
                minuto = datetime.strftime(datas[i], "%M")
                fname = basepath + codigos[i] + '/' + dia + '-' + mes + '-' + ano + '--' + hora + '-' + minuto + '.csv'
                foundDep = False
                with open(fname, 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['_Nome'].upper() == depNome: # encontrei o deputado
                            foundDep = True
                            voto = row['_Voto']
                            if voto == 'Sim':
                                votos.append(1)
                            elif voto == 'Não':
                                votos.append(-1)
                            else:
                                votos.append(0) # abstencao ou outros fatores...
                                zeroCount += 1
                            break
                if not foundDep:
                    # por algum motivo nao encontrei esse deputado nesta votacao
                    zeroCount += 1
                    votos.append(0) 
            if zeroCount < 0.5 * len(datas):
                writer.writerow(votos) # so contabilize deputados que votam...
