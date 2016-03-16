# -*- coding: utf-8 -*-
"""
@author: Cássio
"""

import json

params = json.load(open("src/params.json", "r", encoding = 'UTF-8'))
wd     = params['workingdir']
ano    = params['ano']

