# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:43:04 2016

Obtem resultados de votacoes para as proposicoes de um determinado ano

@author: Cássio
"""

from suds.client import Client
import csv
import time
import random
import os

exec(open("src/python/load_params.py").read())

url = "http://www.camara.gov.br/SitCamaraWS/Proposicoes.asmx?wsdl"

client = Client(url)

escapechar = '\\'

with open(wd + "dados/detalhes-props-" + str(ano) + ".csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile,  lineterminator = '\n', 
                                quoting = csv.QUOTE_NONNUMERIC, 
                                escapechar = escapechar)    
    
    for row in reader:
        # pode haver mais de uma votacao por proposicao...
        idProp = row['idProposicao']
        print("Processando a proposição", str(idProp) + '...')        
        
        votacoes = client.service.ObterVotacaoProposicaoPorID(
            idProposicao = idProp).proposicao.Votacoes.Votacao
    
        # cria diretorio para guardar resultados desta votacao        
        votePropDir = wd + 'dados/' + str(ano) + '/votacoes/' + idProp
        if not os.path.exists(votePropDir):
            os.makedirs(votePropDir)

        if(type(votacoes) == list): # temos mais de uma votacao para essa proposicao
            N = len(votacoes)
        else:
            N = 1    
        
        for i in range(1, N + 1):
            if N > 1:
                deputados = votacoes[i - 1].votos.Deputado                    
                data = votacoes[i - 1]._Data.strip()
                hora = votacoes[i - 1]._Hora.strip()
            else:
               deputados = votacoes.votos.Deputado
               data = votacoes._Data.strip()
               hora = votacoes._Hora.strip()    
            
            # ignore votacoes da proposicao que nao foram feitas
            # no ano de interesse
            # *** assume-se que o ano esta nos ultimos quatro digitos ***
            if data[len(data)-4:len(data)] != str(ano): 
                continue

            with open(votePropDir + '/' + data.replace('/', '-') + "--" + hora.replace(':','-') + ".csv", 'w') as outfile:
                fieldnames = ['idProposicao', '_Data', '_Hora', '_Nome', 
                              '_UF', '_Partido', '_ideCadastro', '_Voto']
                escapechar = '\\'
                writer = csv.DictWriter(outfile, fieldnames = fieldnames, 
                                        lineterminator = '\n', 
                                        quoting = csv.QUOTE_NONNUMERIC, 
                                        escapechar = escapechar)
                writer.writeheader()
            
                        
                
                for dep in deputados:
                    
                    writer.writerow({fieldnames[0] : idProp.strip(),
                                     fieldnames[1] : data,
                                     fieldnames[2] : hora,
                                     fieldnames[3] : dep._Nome.strip(),
                                     fieldnames[4] : dep._UF.strip(),
                                     fieldnames[5] : dep._Partido.strip(),
                                     fieldnames[6] : dep._ideCadastro.strip(),
                                     fieldnames[7] : dep._Voto.strip()})
        
        time.sleep(random.uniform(0,0.2)) # evite DoS :)
