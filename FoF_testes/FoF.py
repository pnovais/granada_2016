'''
Programa criado para determinar os pixels e regioes conexas, utilizando o
conceito de Friends of Friens
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
import hu
import plots

__author__ = 'pnovais'
ini=time.time()


def distancia(x1,y1,x2,y2):
    dm2 = 2.25
    d=0
    dist2 = (x1-x2)**2 + (y1-y2)**2
    if dist2 <= dm2:
        d=1
    print(d)
    return d


ff = pd.read_csv('pop1.csv')

k=0
d = []
df = pd.DataFrame(index=range(0,390625))
for i in range(len(ff)):
    x1 = ff['x'][i]
    y1 = ff['y'][i]
    for j in range(len(ff)):
        x2 = ff['x'][j]
        y2 = ff['y'][j]
        k=k+1
        d.append(distancia(x1,y1,x2,y2))

df['distancia'] = d
print(k)

#distancia(ff)


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
