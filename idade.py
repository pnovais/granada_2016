"""
Programa para determinacao da faixa de idade em cada grupo de galaxias
grupo 1: E, S0
grupo 2: Sa/Sab, Sb, Sbc
grupo 3: Sc, Sd/Irr

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

#definindo a classe que ira ler as imagens fits
def get_image(f_sdss):
    img = f_sdss[0].data
#    sky = f_sdss[2].data
    return img

#abrindo a imagem fits
data_dir = '/home/pnovais/Dropbox/DOUTORADO/granada_2016'
galaxies = pd.read_csv('data/califa_group1.csv')

df2 = pd.DataFrame()
for i_gal in range(len(galaxies)):
    image_age = fits.open('Paty_at_flux__yx/%s_%s.fits' %(galaxies['at-flux'][i_gal],
                                                          galaxies['gal_num'][i_gal]))
    img = get_image(image_age)

    #obtendo os dados da imagem fits
    df0 = pd.DataFrame()
    nrows, ncols = img.shape
    xx, yy = np.meshgrid( *np.ogrid[:ncols, :nrows] )
    table = np.column_stack(( xx.flatten(), yy.flatten(), img.flatten() ))
    temp = pd.DataFrame(table, columns=['x','y','age'])
    df0 = pd.concat([df0,temp], axis=1)

    #selecionando apenas os dados de idade > 0
    df = df0[df0.age > 0.0]

    frames = [df2,df]
    df2 = pd.concat(frames)

print(df2['age'].min())
print(df2['age'].max())
print(df['age'].min())
print(df['age'].max())


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
