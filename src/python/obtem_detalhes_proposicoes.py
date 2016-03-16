# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 13:26:18 2016

@author: Cássio
"""

from suds.client import Client
import csv
import time
import random

exec(open("src/python/load_params.py").read())

url = "http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl"

client = Client(url)

pset = set() # podem existir proposicoes repetidas nas votacoes, controlar aqui

with open(wd + "dados/votadas-" + str(ano) + ".csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    with open(wd + "dados/detalhes-props-" + str(ano) + ".csv", 'w') as outfile:
        fieldnames = ['_numero', '_ano', '_tipo', 'nomeProposicao', 
        'idProposicao', 'tipoProposicao', 'tema', 'Ementa', 'Autor', 
        'DataApresentacao', 'RegimeTramitacao', 'Apreciacao', 'Indexacao',
        'Situacao', 'LinkInteiroTeor']
        escapechar = '\\'
        writer = csv.DictWriter(outfile, fieldnames = fieldnames, 
                                lineterminator = '\n', 
                                quoting = csv.QUOTE_NONNUMERIC, 
                                escapechar = escapechar)
        writer.writeheader()
        
        for row in reader:            
            cod = row['codProposicao']            
            if not cod in pset:
                print("Obtendo dados da proposição " + cod + "...")
                pset.add(cod)
                prop = client.service.ObterProposicaoPorID(idProp = cod)
                if len(prop) > 1:
                    raise ValueError('obtive lista > 1 para a proposicao ' + 
                                      cod +  '! I give up :-(')
                p = prop[0]
                writer.writerow(
                    {fieldnames[0]  : p._numero.strip(),
                     fieldnames[1]  : p._ano.strip(),
                     fieldnames[2]  : p._tipo.strip(),
                     fieldnames[3]  : p.nomeProposicao.strip(),
                     fieldnames[4]  : p.idProposicao.strip(),
                     fieldnames[5]  : p.tipoProposicao.strip(),
                     fieldnames[6]  : p.tema.strip(),
                     fieldnames[7]  : p.Ementa.strip(),
                     fieldnames[8]  : p.Autor.strip(),
                     fieldnames[9]  : p.DataApresentacao.strip(),
                     fieldnames[10]  : p.RegimeTramitacao.strip(),
                     fieldnames[11]  : p.Apreciacao.strip(),
                     fieldnames[12]  : p.Indexacao.strip(),
                     fieldnames[13]  : p.Situacao.strip(),          
                     fieldnames[14]  : p.LinkInteiroTeor.strip()}
                )
                time.sleep(random.uniform(0,0.2)) # evite dos :)
        