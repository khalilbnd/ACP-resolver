# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:20:36 2023

@author: khalil
"""
import numpy as np
from sklearn.decomposition import PCA

def MetricMat(X):
   
    # Calculer la matrice de covariance
    cov_matrix = np.cov(X.T)
    # Effectuer une ACP
    pca = PCA(n_components=1)
    pca.fit(X)
    # Calculer la métrique M
    M = pca.explained_variance_ / cov_matrix.diagonal()
    return M