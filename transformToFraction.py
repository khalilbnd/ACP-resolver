# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:31:19 2023

@author: khalil
"""
from fractions import Fraction


def toFraction2D(V):
    Res = []
    
    for i in V:
        sub_res = []
        for j in i:
            sub_res.append(str(Fraction(j).limit_denominator(1000)))
        
        Res.append(sub_res)
    
    return Res

def toFraction(V):
    Res = []
    
    for i in V:
            Res.append(str(Fraction(i).limit_denominator(1000)))
        
    
    return Res