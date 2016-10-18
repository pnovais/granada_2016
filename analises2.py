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
        df = pd.read_table('data/%s/parametros_hu_%s.txt' %(typeg,param['gal_num'][i]), delim_whitespace = True)
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

    df4 = df2.ix[:,('Raio_medio','Conc','sym')]
    plt.figure()
    df4.plot.box()
    plt.savefig('figures/%s/boxplot_R_C_S_%s.png' %(typeg,typeg))

    df5 = df2.ix[:,(1,14,15,16,17)]
    df5.hist()
    plt.axis
    plt.savefig('figures/%s/teste_%s' %(typeg,typeg))
    plt.clf()

    plt.figure()
    plt.plot(df2.tp, df2.Raio_medio, 'rs', df2.tp, df2.Conc, 'bs')
    plt.savefig('figures/%s/corrs%s.png' %(typeg,typeg))

    return(df2)



early = pd.read_csv('data/group1/califa_group1.csv' )
late = pd.read_csv('data/group2/califa_group2.csv' )
irregular = pd.read_csv('data/group3/califa_group3.csv')

df1 = plots(early,'group1')
df2 = plots(late,'group2')
df3 = plots(irregular,'group3')

plt.figure()
plt.xlim([5,12])
plt.xlabel('Idade da Populacao')
plt.ylim([0,1.2])
plt.ylabel('Concentracao')
plt.plot(df1.tp, df1.Conc, 'rs', df2.tp, df2.Conc, 'bs', df3.tp, df3.Conc,'g^')
plt.savefig('figures/tp_concentration.png')

plt.figure()
plt.xlim([5,12])
plt.xlabel('Idade da Populacao')
plt.ylim([-0.2,1.2])
plt.ylabel('Symmetry')
plt.plot(df1.tp, df1.sym, 'rs', df2.tp, df2.sym, 'bs', df3.tp, df3.sym,'g^')
plt.savefig('figures/tp_symetry.png')

plt.figure()
plt.xlim([5,12])
plt.xlabel('Idade da Populacao')
plt.ylim([0,2])
plt.ylabel('Raio_medio (ponderado)')
plt.plot(df1.tp, df1.Raio_medio, 'rs', df2.tp, df2.Raio_medio, 'bs', df3.tp, df3.Raio_medio,'g^')
plt.savefig('figures/tp_raio_medio.png')

plt.figure()
#plt.xlim([5,12])
plt.ylabel('I1')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.I1, 'rs', df2.Raio_medio, df2.I1, 'bs', df3.Raio_medio, df3.I1,'g^')
plt.savefig('figures/raio_medio_I1.png')

plt.figure()
#plt.xlim([5,12])
plt.ylabel('I5')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.I5, 'rs', df2.Raio_medio, df2.I5, 'bs', df3.Raio_medio, df3.I5,'g^')
plt.savefig('figures/raio_medio_I5.png')

plt.figure()
#plt.xlim([5,12])
plt.ylabel('I6')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.I6, 'rs', df2.Raio_medio, df2.I6, 'bs', df3.Raio_medio, df3.I6,'g^')
plt.savefig('figures/raio_medio_I6.png')

plt.figure()
#plt.xlim([5,12])
plt.ylabel('I7')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.I7, 'rs', df2.Raio_medio, df2.I7, 'bs', df3.Raio_medio, df3.I7,'g^')
plt.savefig('figures/raio_medio_I7.png')

plt.figure()
#plt.xlim([5,12])
plt.ylabel('flong')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.flong, 'rs', df2.Raio_medio, df2.flong, 'bs', df3.Raio_medio, df3.flong,'g^')
plt.savefig('figures/raio_medio_flong.png')


plt.figure()
#plt.xlim([5,12])
plt.ylabel('Concentracao')
plt.xlim([0,2])
plt.xlabel('Raio_medio (ponderado)')
plt.plot(df1.Raio_medio, df1.Conc, 'rs', df2.Raio_medio, df2.Conc, 'bs', df3.Raio_medio, df3.Conc,'g^')
plt.savefig('figures/raio_medio_Conc.png')


plt.figure()
plt.xlim([5,12])
plt.xlabel('Idade media - galaxia')
plt.ylim([-0.2,1.2])
plt.ylabel('Flong')
plt.plot(df1.tm, df1.flong, 'rs', df2.tm, df2.flong, 'bs', df3.tm, df3.flong,'g^')
plt.savefig('figures/tm_flong.png')


plt.figure()
#plt.xlim([5,12])
plt.xlabel('I1')
#plt.ylim([-0.2,1.2])
plt.ylabel('Major semi-axis')
plt.plot(df1.I1, df1.a, 'rs', df2.I1, df2.a, 'bs', df3.I1, df3.a,'g^')
plt.savefig('figures/I1_a.png')


c = np.corrcoef(df2)
print(c)

fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
