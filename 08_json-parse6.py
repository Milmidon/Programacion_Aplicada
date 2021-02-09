# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:26:28 2021

@author: idga-
"""

import urllib.parse
import requests 

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "fZ5mwMBDA6WukqNHZZLiILoV2aHtUfa9"
#The "while True" construct creates an  endless loop.
while True: 
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    
    dest = input("Destion: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to":dest})
    print("URL: " + (url))
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from " + (orig) + "to" + (dest))
        print("Trip Duration:  " + str(json_data["route"]["formattedTime"]))
        print("Kilometers:     " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used(Ltr)  " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + "(" + str("{:.2f}".format((each["disctance"])+1.61) + "km"))
        print("===========================================\n")