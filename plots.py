
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


def juncao(param,typeg):
    #criando um dataframe com os dados de todas as galaxias
    df2 = pd.DataFrame()
    plt.close()
    for i in range(len(param)):
        df = pd.read_table('data/parametros_hu_%s.txt' %(param['gal_num'][i]), delim_whitespace = True)
    #   df.columns = ['Pop','Raio_medio','std_R','tm','tm_std','tp','tp_std','M_t', 'M_p', 'I1','I2','I3','I4','I5','I6','I7','a','b','f=a+b/2','tetha','Excent','flong','sym','Conc']
        frames = [df2,df]
        df2 = pd.concat(frames)
    df2.to_csv('data/all_parameters_%s.csv' %(typeg))

    plt.figure()
    df2.hist()
    plt.savefig('figures/histograms_all_%s.png' %(typeg))
    #histograma dos momentos de hu
    df3 = df2.ix[:,('I1','I2','I3','I4','I5','I6','I7')]
    df3.plot.hist(bins=50)
    plt.savefig('figures/hist_hu_all_on_one_%s.png' %typeg)
    plt.figure()
    df3.plot.kde()
    plt.savefig('figures/kde_hu_all_on_one_%s.png' %(typeg))
    return(df2)

def compare(df1, df2, df3):
    plt.close()
    plt.figure()
    plt.xlim([5,12])
    plt.xlabel('Idade da Populacao')
    plt.ylim([0,1.2])
    plt.ylabel('Concentracao')
    plt.plot(df1.tp, df1.Conc, 'rs', df2.tp, df2.Conc, 'bs', df3.tp, df3.Conc,'g^')
    plt.savefig('figures/tp_concentration.png')
