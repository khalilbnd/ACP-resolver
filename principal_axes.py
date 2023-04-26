# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:31:40 2023

@author: khalil
"""

import numpy as np

def PrincipalAxes(V):
    # Calculer les valeurs propres et vecteurs propres de la matrice de covariance
    eig_vals, eig_vecs = np.linalg.eig(V)
    # Trier les vecteurs propres en ordre décroissant des valeurs propres correspondantes
    idx = eig_vals.argsort()[::-1]
    eig_vecs = eig_vecs[:, idx]
    return eig_vecs