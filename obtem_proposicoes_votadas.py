# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 13:00:16 2016

@author: Cássio
"""

from suds.client import Client
import csv

ano = 2015

url = "http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl"

wd = "C:/Users/Cássio/Dropbox/analise-votacoes/"

client = Client(url)

propos = client.service.ListarProposicoesVotadasEmPlenario(ano = ano)

ps = propos.proposicoes[0]

with open(wd + "votadas-" + str(ano) + ".csv", 'w') as csvfile:
    fieldnames = ['codProposicao', 'nomeProposicao', 'dataVotacao']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames, lineterminator = '\n')

    writer.writeheader()
    for p in ps:
        writer.writerow({fieldnames[0]  : p.codProposicao,
                         fieldnames[1] : p.nomeProposicao,
                         fieldnames[2]    : p.dataVotacao})
