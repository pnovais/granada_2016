#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
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
import hu

__author__ = 'pnovais'
ini=time.time()

data_dir = '/home/pnovais/Dropbox/DOUTORADO/granada_2016'
galaxies = pd.read_table('Paty_at_flux__yx/mapas.txt', delim_whitespace = True)
galaxies.columns = ['at_flux', 'gal_num']

for i in range(len(galaxies)):
    df= pd.read_table('data/parametros_hu_%s.txt' %galaxies['gal_num'][i], delim_whitespace = True)
    df.columns = ['#Populacao','Rm/re','std','I1','I2','I3','I4','I5','I6','I7','a','b','f=a+b/2','tetha','Exc','flong','Sim','Conc']
    df2 = df.ix[:,('Rm/re','I1','I2','I3','I4','I5','I6','I7','a','b','tetha','Exc','flong','Sim','Conc')]

    corr=df2.corr(method='pearson')
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr,mask=mask)
    plt.title('galaxy_%s' %galaxies['gal_num'][i])
    plt.savefig('figures/Correlations_%s.png' %galaxies['gal_num'][i])
    print(i)


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
