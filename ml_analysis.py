"""
Rotina para analisar os dados obtidos com a rotina granada.py
30/09/16
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


def plots(param,typeg):
    #criando um dataframe com os dados de todas as galaxias
    df2 = pd.DataFrame()
    for i in range(len(param)):
        df = pd.read_table('data/parametros_hu_%s.txt' %param['gal_num'][i], delim_whitespace = True)
        df.columns = ['Pop','Raio_medio','std_R','I1','I2','I3','I4','I5','I6','I7',
                      'a','b','f=a+b/2','tetha','Excent','flong','sym','Conc']
        df3 = param['gal_num'][i]
        frames = [df2,df]
        df2 = pd.concat(frames)
        #df7 = df2.ix[df2['Pop'] == 2]
        df8 = df2.ix[df2['Pop'] == 3]

    df2.to_csv('all_parameters_allgalaxies_%s.csv' %typeg)

    #gerando os histogramas
    plt.figure()
    df2.hist()
    plt.savefig('figures/histograms_all_%s.png' %typeg)

    #histograma dos momentos de hu
    df3 = df2.ix[:,('I1','I2','I3','I4','I5','I6','I7')]

    '''plt.figure()
    df3.plot.hist(bins=1500)
    plt.xlim(-2,4)
    plt.savefig('figures/hist_hu_all_on_one.png')
    '''

    plt.figure()
    df3.hist('I7', bins=900)
    plt.xlim(-2,2)
    plt.savefig('figures/hist_hu_I7_%s.png' %typeg)

    plt.figure()
    df3.plot.box()
    plt.ylim(-1,2)
    plt.savefig('figures/boxplot_hu_all_on_one_%s.png' %typeg)


    plt.figure()
    df3.plot.kde()
    plt.xlim(-4,5)
    plt.savefig('figures/kde_hu_all_on_one_%s.png' %typeg)

    df4 = df2.ix[:,('Raio_medio','Conc','sym')]
    plt.figure()
    df4.plot.box()
    plt.savefig('figures/boxplot_R_C_S_%s.png' %typeg)

    df5 = df2.ix[:,(1,14,15,16,17)]
    df5.hist()
    #plt.title("my title", x=0.5, y=0.2)
    plt.axis
    plt.savefig('figures/teste_%s' %typeg)
    plt.clf()
    #return df2




#lendo o arquivo com o nomes dos arquivos de parametros
data_dir = '/home/pnovais/Dropbox/DOUTORADO/granada_2016'
late = pd.read_csv('califa_gal_properts_late.csv')
early = pd.read_csv('califa_gal_properts_early.csv')
all_type = pd.read_csv('califa_gal_properts.csv')


#param.columns = ['arq', 'gal_num']


#early = propers.ix[(propers['u-r'] > 2.22)]
#late = propers.ix[propers['u-r'] < 2.22]

plots(late,'late')
plots(early,'early')
plots(all_type,'all')





fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
