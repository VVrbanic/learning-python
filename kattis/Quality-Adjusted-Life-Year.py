# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:42:51 2019

@author: Vera
"""

n=input()
a=0
for i in range (0, int(n)):
    y,q=map(float,input().split())
    a=a+y*q
print(a)
    
