"""
Programa para analise dos mapas de idade do CALIFA, utilizando a pipeline x.x
17/10/16

Versao 0.0
"""

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


grupo='group3'

def plots(param,typeg):
    #criando um dataframe com os dados de todas as galaxias
    df2 = pd.DataFrame()
    for i in range(len(param)):
        df = pd.read_table('data/%s/parametros_hu_%s.txt' %(grupo,param['gal_num'][i]), delim_whitespace = True)
        df.columns = ['Pop','Raio_medio','std_R','tm','tm_std','tp','tp_std','I1','I2','I3','I4','I5','I6','I7',
                      'a','b','f=a+b/2','tetha','Excent','flong','sym','Conc']
        frames = [df2,df]
        df2 = pd.concat(frames)

    df2.to_csv('data/%s/all_parameters_%s.csv' %(typeg,typeg))
    #gerando os histogramas
    plt.figure()
    df2.hist()
    plt.savefig('figures/%s/histograms_all_%s.png' %(typeg,typeg))

    #histograma dos momentos de hu
    df3 = df2.ix[:,('I1','I2','I3','I4','I5','I6','I7')]
    df3.plot.hist(bins=50)
    #plt.xlim(-2,4)
    plt.savefig('figures/%s/hist_hu_all_on_one.png' %typeg)

    plt.figure()
    df3.plot.kde()
    #plt.xlim(-4,5)
    plt.savefig('figures/%s/kde_hu_all_on_one_%s.png' %(typeg,typeg))


late = pd.read_csv('data/%s/califa_%s.csv' %(grupo,grupo))

plots(late,grupo)


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
