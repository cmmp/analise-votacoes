# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 20:29:51 2016

@author: Cássio
"""

import csv
import time
import random

from urllib.request import urlretrieve

exec(open("src/python/load_params.py").read())

with open(wd + "dados/deputados.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("Obtendo foto para deputado", row['nomeParlamentar'])
        urlretrieve(row['urlFoto'], wd + "html/fotos/" + row['ideCadastro'] + ".jpg")
        time.sleep(random.uniform(0, 0.2)) # no DoS on the gov :)       
