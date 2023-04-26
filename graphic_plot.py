# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:27:23 2023

@author: khalil
"""

import numpy as np
import matplotlib.pyplot as plt

def GraphicPlot(C):
    # Récupérer les coordonnées des composantes principales
    x = C[:, 0]
    y = C[:, 1]
    # Créer le graphique
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    # Ajouter des étiquettes pour chaque point
    for i, txt in enumerate(range(len(x))):
        ax.annotate(txt, (x[i], y[i]))
    # Ajouter des titres aux axes
    ax.set_xlabel('Composante principale 1')
    ax.set_ylabel('Composante principale 2')
    # Afficher le graphique
    plt.show()