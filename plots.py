
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

    plt.figure()
    plt.xlim([5,12])
    plt.xlabel('Idade da Populacao')
    plt.ylim([-0.2,1.2])
    plt.ylabel('Symmetry')
    plt.plot(df1.tp, df1.Sim, 'rs', df2.tp, df2.Sim, 'bs', df3.tp, df3.Sim,'g^')
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
