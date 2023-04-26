# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:22:17 2023

@author: khalil
"""

import numpy as np

def ComposantsPrincipale(X_centered, U):
    # Calculer les composantes principales
    C = np.dot(X_centered, U)
    return C