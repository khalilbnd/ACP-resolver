# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:13:51 2023

@author: khalil
"""
from fractions import Fraction

import numpy as np
def varianceCovarianceMat(X_centered):
    # Calculer la matrice de covariance
    V = np.dot(X_centered.T, X_centered) / X_centered.shape[0]
   # for i in range(len(V)):
   #     for j in range(len(i)) :
           
    #        V[i][j] = Fraction(V[i][j]).limit_denominator()
    return V