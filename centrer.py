import numpy as np

def centerMat(X):
    # Calculer la moyenne de chaque colonne de X
    g = np.mean(X, axis=0)
    # Calculer la matrice centrée X'
    X_centered = X - g
    return X_centered