# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:34:05 2021

@author: Usuario
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Riobamba"
key =  "kM8pfDeZAuLe1XMcZn8nPDkrmukgcWE0"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)