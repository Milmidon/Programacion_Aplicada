# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:23:09 2020

@author: Usuario
"""

print()
aclNUM = int(input('¿Cual es el número del IPv4 ACL? \t'))
print()
if aclNUM >= 1 and aclNUM <= 99:
    print("Este es un estándar IPv4 ACL")
elif aclNUM >= 100 and aclNUM <= 199:
    print("Este es una extensión IPv4 ACL")
else:
    print("Este no es un estándar o una extensión IPv4 ACL")