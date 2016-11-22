'''
Programa criado para determinar os pixels e regioes conexas, utilizando o
conceito de Friends of Friens 02
21/11/2016
Autora: Patricia Novais
'''

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

__author__ = 'pnovais'
ini=time.time()


def distancia(x1,y1,x2,y2):
    dm2 = 2.25
    d=0
    dist2 = (x1-x2)**2 + (y1-y2)**2
#    if dist2 <= dm2:
#        d=1
    #print(d)
    return d


ff = pd.read_csv('pop1.csv')

'''l = 1
k=0
d = []
values = [i for i in range(len(ff))]
data = {'Index_g': values}
idx_group = pd.DataFrame(data)
ngroup = 0
ii = 0
'''
dx = []
dy = []
values = [i for i in range(0,80*80)]
data = {'ind': values}
df = pd.DataFrame(data)

for i in range(0,80):
    for j in range(0,80):
        dx.append(j)
        dy.append(i)

df['x'] = dx
df['y'] = dy

'''
for i in range(len(ff)):
    x1 = ff['x'][i]
    y1 = ff['y'][i]
   for j in range(i,len(ff)):
        x2 = ff['x'][j]
        y2 = ff['y'][j]
        k=k+1
        dd = distancia(x1,y1,x2,y2)
        if (dd <= 1):
            if (idx_group['Index_g'][i] == 0 and idx_group['Index_g'][j] == 0):
                ngroup = ngroup + 1
                idx_group['Index_g'][i] = float(ngroup)
                idx_group['Index_g'][j] = float(ngroup)
            else:
                if (idx_group['Index_g'][i] == 0 and idx_group['Index_g'][j] > 0):
                    ii = idx_group['Index_g'][j]
                if (idx_group['Index_g'][i] > 0 and idx_group['Index_g'][j] == 0):
                    ii = idx_group['Index_g'][i]
                if (idx_group['Index_g'][i] > 0 and idx_group['Index_g'][j] > 0):
                    ii = min(idx_group['Index_g'][i],idx_group['Index_g'][j])
            idx_i = idx_group['Index_g'][i]
            idx_j = idx_group['Index_g'][j]
            idx_group['Index_g'][i] = ii
            idx_group['Index_g'][i] = ii
            for k in range(len(ff)):
                if ((idx_i > 0) and (idx_group['Index_g'][k] == idx_i)):
                    idx_group['Index_g'][k] = ii
                if ((idx_j > 0) and (idx_group['Index_g'][k] == idx_j)):
                    idx_group['Index_g'][k] = ii
'''

fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
