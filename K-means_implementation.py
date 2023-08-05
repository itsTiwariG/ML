# -*- coding: utf-8 -*-
"""K-Means implementation from scratch

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rzTJ0Qke1OPAuHm1oaYpv6G5Uo-HZ_X3
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler


class Kmeans:
    '''Intialize the parameters as for K - means clustering'''
    def __init__(self,no_clusters,co_ordinates,max_iterations):
        self.no_clusters = no_clusters
        self.co_ordinates = co_ordinates
        self.max_iterations = max_iterations
    '''Cluster the data'''
    def Train(self,X):
        classes = []

        # TO Check if there is any significant difference between previous two co_ordinates
        flag = True

        # Iterate till max_iterations is reached
        for i in range(self.max_iterations):

            classes = self.predict(X)
            flag = self.new_clusters(classes,X)

            # If there is no significant difference between previous two co_ordinatess return co_ordinates
            if(flag):
                continue
            else:
                break
        return self.co_ordinates

    def predict(self,X):
        # Assign each data point to the closest cluster center
        clusters = np.zeros(X.shape[0])
        for i, x in enumerate(X):
            distances =np.sqrt(np.sum((x - self.co_ordinates)**2, axis=1))
            cluster = np.argmin(distances)
            clusters[i] = cluster
        return clusters

    '''change cluster to the mean of data points of that cluster'''
    def new_clusters(self,classes,X):

        old_cor = self.co_ordinates
        for i in range(0,self.no_clusters):

            # Iterate over each  claster
            X_c = X[classes == i]
            if(len(X_c)>0):
                self.co_ordinates[i,:] = np.mean(X_c, axis=0)
            else:

            # If there are no points in that cluster assign a new random point from the give datapoints
                self.co_ordinates[i,:] =  X[np.random.choice(len(X), 1 ,replace= False)]

        # If the co_ordinates are close enough
        if np.allclose(old_cor,self.co_ordinates,rtol=1e-4):
            return False
        else:
            return True

        '''Calculate the sum of squared error'''
    def score(self,X,pred_classes):
        dist = 0
        for c in np.unique(pred_classes):
            X_c = X[ pred_classes == c ]
            for sample in X_c:
                dist += np.linalg.norm(sample-self.co_ordinates[int(c),:])**2
        return dist

