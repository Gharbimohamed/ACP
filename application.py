import os
import random
import sklearn
from sklearn.preprocessing import StandardScaler
import numpy
from sklearn.decomposition import PCA
print("nombre de lignes")
x= input()
x1= int(x)
print("le nombre de colonnes")
y= input()
y1= int(y)
C = [[0]*y1 for i in range(x1)] # matrice de b lignes et m colonnes
# parcourir les lignes
for i in range(x1):
# parcourir les colonnes
    for j in range(y1):
        rnd= random.randint(1, 20)
        C[i][j]= rnd
print(C)
sc = StandardScaler()
Z = sc.fit_transform(C) 
print(Z)
print(numpy.mean(Z,axis=0))
print(numpy.std(Z,axis=0,ddof=0))
acp = PCA(svd_solver='full')
coord = acp.fit_transform(Z)
print(acp.n_components_)
print(acp.explained_variance_)
eigval = (x1-1)/x1*acp.explained_variance_ 
print(eigval)
print(acp.singular_values_**2/x1)
print(acp.explained_variance_ratio_)
os.system("pause")