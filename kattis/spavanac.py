# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:36:21 2019

@author: Vera
"""

s, m = map(int, input().split())
1
if m< 45 and s==0:
        s=23
        m= 15+m
elif m<45:
        s=s-1
        m= 15+m 
else:
        m=m-45
    
print(s,m)
