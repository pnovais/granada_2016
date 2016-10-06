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

def leitura(param):
    df2 = pd.DataFrame()
    for i in range(len(param)):
        df = pd.read_table('data/parametros_hu_%s.txt' %param['gal_num'][i], delim_whitespace = True)
        df.columns = ['Pop','Raio_medio','std_R','I1','I2','I3','I4','I5','I6','I7',
                      'a','b','f=a+b/2','tetha','Excent','flong','sym','Conc']
        agreg = []
        for j in range(len(df)):
            agreg.append(param['gal_num'][i])
        df['gal'] = agreg
        frames = [df2,df]
        df2 = pd.concat(frames)



#lendo o arquivo com o nomes dos arquivos de parametros
data_dir = '/home/pnovais/Dropbox/DOUTORADO/granada_2016'
late = pd.read_csv('califa_gal_properts_late.csv')
early = pd.read_csv('califa_gal_properts_early.csv')
all_type = pd.read_csv('califa_gal_properts.csv')


leitura(late)


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
