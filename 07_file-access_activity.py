# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:00:02 2021

@author: Usuario
"""

file=open("devices.txt","a")
while True:
    newItem=input('Usuario ingrese un nuevo dispositivo, sino poner exit: ')
    if newItem == 'exit':
        print("Todo listo!")
        break
    else:
        file.write(newItem+"\n")
print('devices.txt')
file.close()
