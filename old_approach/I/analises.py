#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
import datetime
import time
from sys import exit
from matplotlib import colors, pyplot as plt
from functools import reduce
import matplotlib.cm as cm
import seaborn as sns
from astropy.io import ascii, fits
from astropy.wcs import wcs
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.interpolate import interp2d
import cubehelix
import matplotlib.mlab as mlab
import scipy, pylab
import math

__author__ = 'pnovais'
ini=time.time()

def graficos(df,label):
    df2 = df.ix[:,('Pop','R_med','I1','I2','I3','I4','I5','I6','I7','a','b','flong','sym','Conc')]
    df3 = df.ix[:,('I1','I2','I3','I4','I5','I6','I7')]
    df4 = df.ix[:,(2,16,17,18)]
    print('=======================================')
    print(label.upper())
    #print(df2.head())
    label2='parameters'
    label3='hu'
    label4='RCSF'
    correlat(df2,label,label2)
    correlat(df3,label,label3)
    correlat(df4,label,label4)

    scatter_matrix(df2,diagonal='kde')
    plt.savefig('figures/scatter_param_%s.png' %label)

    scatter_matrix(df3,diagonal='kde')
    plt.savefig('figures/scatter_Hu_%s.png' %label)

    scatter_matrix(df4,diagonal='kde')
    plt.savefig('figures/scatter_RCSF_%s.png' %label)


def correlat(df, label, label2):
    corr=df.corr(method='pearson')
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr,mask=mask)
    plt.title('Correlation Matrix - %s: %s-type galaxies' %(label,label2))
    plt.savefig('figures/Correlations_%s_%s.png' %(label,label2))




dfs1 = pd.read_csv('all_parameters_allgalaxies_early.csv')
dfs2 = pd.read_csv('all_parameters_allgalaxies_late.csv')
dfs3 = pd.read_csv('all_parameters_allgalaxies_all.csv')


graficos(dfs1,'early')
graficos(dfs2,'late')
graficos(dfs3,'all')

ax = dfs1.plot(kind='scatter', x='sym',y='Conc', color='blue',label='um')
dfs2.plot(kind='scatter', x='sym',y='Conc', color='red',label='dois')
dfs3.plot(kind='scatter', x='sym',y='Conc', color='green',label='all', s=4)




fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
