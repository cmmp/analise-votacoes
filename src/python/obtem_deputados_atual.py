# -*- coding: utf-8 -*-
"""
Obtem a lista dos deputados em exercicio da camara dos deputados
"""

from suds.client import Client
import csv

exec(open("src/python/load_params.py").read())

url = "http://www.camara.gov.br/SitCamaraWS/Deputados.asmx?wsdl"

client = Client(url)

deps = client.service.ObterDeputados()
deplist = deps.deputados[0]

with open(wd + 'dados/deputados.csv', 'w') as outfile:
    fieldnames = ['ideCadastro', 'condicao', 'matricula', 'idParlamentar',
                  'nome', 'nomeParlamentar', 'urlFoto', 'sexo', 'uf',
                  'partido', 'gabinete', 'anexo', 'fone', 'email']
    escapechar = '\\'
    writer = csv.DictWriter(outfile, fieldnames = fieldnames, 
                        lineterminator = '\n', 
                        quoting = csv.QUOTE_NONNUMERIC, 
                        escapechar = escapechar)
    writer.writeheader()

    for d in deplist:
        writer.writerow({fieldnames[0] : d.ideCadastro.strip(),
                         fieldnames[1] : d.condicao.strip(),                         
                         fieldnames[2] : d.matricula.strip(),
                         fieldnames[3] : d.idParlamentar.strip(),
                         fieldnames[4] : d.nome.strip(),
                         fieldnames[5] : d.nomeParlamentar.strip(),
                         fieldnames[6] : d.urlFoto.strip(),
                         fieldnames[7] : d.sexo.strip(),
                         fieldnames[8] : d.uf.strip(),
                         fieldnames[9] : d.partido.strip(),
                         fieldnames[10] : d.gabinete.strip(),
                         fieldnames[11] : d.anexo.strip(),
                         fieldnames[12] : d.fone.strip(),
                         fieldnames[13] : d.email.strip(),
                         })
