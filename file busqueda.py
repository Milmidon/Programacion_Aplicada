# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:08:19 2021

@author: idga-
"""
file=open('devices.txt')
for a in file:
    a=a.strip()
    print(a)
file.close