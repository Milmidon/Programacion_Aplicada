# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:00:52 2020

@author: idga-
"""

aclNum=int(input("what is the Ipv4 ACL number"))
if aclNum>=1 and aclNum <=99:
    print("This is a standard IPv4 ACl.")
elif aclNum >=100 and aclNum <=199:
    print("This is a extended Ipv4 ACL.")
else:
    print("This is not a standad or extended IPv4")
