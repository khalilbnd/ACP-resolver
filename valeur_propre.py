# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:13:12 2023

@author: khalil

"""

import numpy as np

def ValeurPropre(V):
    # Calculer les valeurs propres de la matrice de covariance
    eig_vals = np.linalg.eigvals(V)
    # Trier les valeurs propres en ordre décroissant
    idx = eig_vals.argsort()[::-1]
    eig_vals = eig_vals[idx]
    # Calculer la proportion de variance pour chaque axe principal
    var_prop = eig_vals / np.sum(eig_vals)
    return eig_vals, var_prop