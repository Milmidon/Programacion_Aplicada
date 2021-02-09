# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:27:27 2020

@author: Usuario
"""
print("¡BIENVENIDO!")
print()
print("Has sido seleccionado para participar por un automovil 0 Km para el 2021. \nIngresa tus datos a continuación")
nombre = input("Ingresa tus nombres completos: ")
apellido = input("Ingresa tus apellidos completos: ")
ciudad = input("Verifica en que ciudad vives: ")
correo = input("Inserta tu correo electrónico:\n")
print("Ya casi estan completos tus datos ,unicamente necesitamos un dato más... \n")
edad = int(input("Dinos que edad tienes: "))

if edad <=17 :
    print()
    print('Lo siento mucho pero al tener',edad,'te consideramos MENOR DE EDAD \n')
    print('En unos años podrías participar de nuevo en el Concurso.')
elif edad >= 18 and edad <= 60 :
    print()
    print('FELICITACIONES', nombre, apellido, '\nAhora podrás disfrutar de tu Nuevo Auto 0 Km')
    print('Te estaremos visitando en tu ciudad', ciudad, '\nY te notificaremos la fecha que estaremos alli por medio del correo:',correo)
    print('Y te deseamos el mejor de los exitos en este 2021')
else:
    print()
    print('Usted es considerado como un ADULTO MAYOR al tener',edad,'años.\nPor lo que le daremos otra opción para el premio. \nEn su caso será 20 dolares de compra en Supermaxi')
    print('Y te deseamos el mejor de los exitos en este 2021')