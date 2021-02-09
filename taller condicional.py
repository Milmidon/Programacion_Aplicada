# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:34:14 2020

@author: idga-
"""

nombre=input("Ingrese su Primer Nombre")
apellido=input("Ingrese su Primer Apellido")
edad=input("Ingrese su edad")
ciudad=input("Ingrese la ciudad de resisdencia")
print("Hola",nombre,apellido,"Vives en",ciudad)
if edad>=1 and edad <=6:
    print("Eres un bebé ")
elif edad >=7 and edad <=12:
    print("Eres un buen niño ")
elif edad >=13 and edad <=17:
    print("Eres adolescente")
elif edad >=18 and edad <= 26:
    print("Eres joven")
elif edad >= 27 and edad <= 33:
    print("Eres adulto")
elif edad >=34 and edad <= 45:
    print("Eres adulto senior")
else:
    print("Eres adulto mayor")