# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:34:11 2021

@author: idga-
"""

import urllib.parse
import requests 
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "fZ5mwMBDA6WukqNHZZLiILoV2aHtUfa9"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)
