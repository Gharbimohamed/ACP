
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import pandas
import sklearn
from sklearn.preprocessing import StandardScaler
import numpy
from sklearn.decomposition import PCA
import matplotlib
import matplotlib.pyplot as plt
def importdufich():
    filename= QtWidgets.QFileDialog.getOpenFileName()
    path= filename[0]
    return path
def direct (path) :
    X = pandas.read_excel(path,sheet_name=0,header=0,index_col=0)
    n = X.shape[0]
    p = X.shape[1]
    sc = StandardScaler()
    Z = sc.fit_transform(X) 
    print(Z)
    print(numpy.mean(Z,axis=0))
    print(numpy.std(Z,axis=0,ddof=0))
    acp = PCA(svd_solver='full')
    coord = acp.fit_transform(Z)
    print(acp.n_components_)
    print(acp.explained_variance_)
    eigval = (n-1)/n*acp.explained_variance_ 
    print(eigval)
    print(acp.singular_values_**2/n)
    print(acp.explained_variance_ratio_)
    return X
def tableau1(X):
    print(X)


app = QtWidgets.QApplication([])
dlg = uic.loadUi("fichier.ui")
dlg.confirmer.clicked.connect(direct(importdufich()))
dlg.pushButton.clicked.connect(tableau1(direct(path)))

dlg.show()
app.exec()

