'''
Programa criado para gerar os dados, pixel a pixel, para as galaxias do CALIFA:
-Idade estelar ponderada pela luminosidade
-Densidade de massa
-Halpha
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

__author__ = 'pnovais'
ini=time.time()

#definindo a classe que ira ler as imagens fits
def get_image(f_sdss):
    img = f_sdss[0].data
#    sky = f_sdss[2].data
    return img


data_dir = '/home/pnovais/Dropbox/DOUTORADO/granada_2016'
#grupo = 'group3'
age = pd.read_csv('Paty_at_flux__yx/age.csv')
mass = pd.read_csv('PatImages/mass.csv')
halpha = pd.read_csv('Hamaps/halpha.csv')

#image_age = fits.open('Paty_at_flux__yx/at_flux__yx_K0002.fits')

#exit()

#for i_gal in range(len(age)):
for i_gal in range(0,4):
    image_age = fits.open('Paty_at_flux__yx/at_flux__yx_%s.fits' %age['num_gal'][i_gal])
    #image_age = fits.open('at_flux__yx_K0127_original.fits')
    img = get_image(image_age)

    #plotando a imagem fits
    plt.figure(1)
    plt.clf()
    cx = cubehelix.cmap(reverse=True, start=0., rot=-0.5)
    imgplot = plt.imshow(100*np.log10(img/255), cmap=cx)
    titulo='Galaxy %s ' %age['num_gal'][i_gal]
    plt.title(titulo)
    plt.colorbar()
    figura = 'figures2/galaxy_%s' %age['num_gal'][i_gal]
    plt.savefig(figura)

    #obtendo os dados da imagem fits
    df_age = pd.DataFrame()
    nrows, ncols = img.shape
    xx, yy = np.meshgrid( *np.ogrid[:ncols, :nrows] )
    table = np.column_stack(( xx.flatten(), yy.flatten(), img.flatten() ))
    temp = pd.DataFrame(table, columns=['x','y','age'])
    df_age = pd.concat([df_age,temp], axis=1)

    image_mass = fits.open('PatImages/PatImagesMcorSD__yx_%s.fits' %age['num_gal'][i_gal])
    #image_age = fits.open('at_flux__yx_K0127_original.fits')
    img = get_image(image_age)

    #obtendo os dados da imagem fits
    df_mass = pd.DataFrame()
    nrows, ncols = img.shape
    xx, yy = np.meshgrid( *np.ogrid[:ncols, :nrows] )
    table = np.column_stack(( xx.flatten(), yy.flatten(), img.flatten() ))
    temp = pd.DataFrame(table, columns=['x','y','mass'])
    df_mass = pd.concat([df_mass,temp], axis=1)
    

fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
