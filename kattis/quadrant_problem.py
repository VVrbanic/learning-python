# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:42:51 2019

@author: Vera
"""
x=input()
y=input()
if int(x) > 0: 
    if int(y) > 0:
        print(1) 
    else:
        print(4)
if int(x) < 0:
    if int(y) > 0:
        print(2)
    else:
        print(3)

