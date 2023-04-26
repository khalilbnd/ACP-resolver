import numpy as np
from centrer import centerMat
from var_covar_matrix import varianceCovarianceMat
from metric import MetricMat
from principal_axes import PrincipalAxes
from quality_representation import QualityRepresentation
from valeur_propre import ValeurPropre
from principal_components import ComposantsPrincipale
from graphic_plot import GraphicPlot

from transformToFraction import toFraction, toFraction2D


X = np.array([[2, 3], [4, 5], [6, 1]])
print("Matrice originale X :")
print(X)
print("---------------------------")
X_centered = centerMat(X)
print("Matrice centrée X' :")
print(toFraction2D(X_centered))
print("---------------------------")

V = varianceCovarianceMat(X_centered)
print("Matrice variance-covariance V :")
print(toFraction2D(V))

print("---------------------------")

M = MetricMat(X_centered)
print("Metric M :")
print(toFraction(M))

print("---------------------------")

PA = PrincipalAxes(V)
print("les axes principal:")
print(PA)

print("---------------------------")

eig_vals, var_prop = ValeurPropre(V)
QR = QualityRepresentation(eig_vals, var_prop)
print("Valeurs propres :")
print(toFraction(eig_vals))
print("Proportion de variance pour chaque axe principal :")
print(toFraction(var_prop))

print("Qualité de représentation Q :")
print(toFraction(QR))

print("---------------------------")

C = ComposantsPrincipale(X_centered, PA)
print("Composantes principales :")
print(C)

GraphicPlot(C)
