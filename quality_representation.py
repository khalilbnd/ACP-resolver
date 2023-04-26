# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:07:31 2023

@author: khalil
"""

import numpy as np

def QualityRepresentation(eig_vals, var_prop, threshold=0.8):
    # Calculer la qualité de représentation pour chaque variable j
    Q = np.zeros(len(eig_vals))
    for j in range(len(eig_vals)):
        Q[j] = np.sum(eig_vals[:j+1]) / np.sum(eig_vals)
        if Q[j] >= threshold:
            break
    return Q