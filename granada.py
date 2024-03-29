"""
Programa para determinacao dos parametros de analise, utilizando os mapas de
idade do CALIFA (idade estelar ponderada pela luminosidade - pipeline x.x)
29/09/16

Versao 0.0

------------------------
Versao 0.1
Com correlacao entre os parametros

-----------------------
Versao 0.2
Separacao por tipo morfologico
(utilizando a rotina selection.py)

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
grupo = 'group3'
galaxies = pd.read_csv('data/%s/califa_%s.csv' %(grupo,grupo))
#galaxies.columns = ['at_flux', 'gal_num']
colunas = ('x','y','age')

for i_gal in range(len(galaxies)):
    image_age = fits.open('Paty_at_flux__yx/%s_%s.fits' %(galaxies['at-flux'][i_gal],
                                                          galaxies['gal_num'][i_gal]))
    #image_age = fits.open('at_flux__yx_K0127_original.fits')
    img = get_image(image_age)

    #plotando a imagem fits
    plt.figure(1)
    plt.clf()
    cx = cubehelix.cmap(reverse=True, start=0., rot=-0.5)
    imgplot = plt.imshow(100*np.log10(img/255), cmap=cx)
    titulo='Galaxy %s ' %galaxies['gal_num'][i_gal]
    plt.title(titulo)
    plt.colorbar()
    figura = 'figures/%s/galaxy_%s' %(grupo,galaxies['gal_num'][i_gal])
    plt.savefig(figura)

    #obtendo os dados da imagem fits
    df0 = pd.DataFrame()
    nrows, ncols = img.shape
    xx, yy = np.meshgrid( *np.ogrid[:ncols, :nrows] )
    table = np.column_stack(( xx.flatten(), yy.flatten(), img.flatten() ))
    temp = pd.DataFrame(table, columns=['x','y','age'])
    df0 = pd.concat([df0,temp], axis=1)

    #selecionando apenas os dados de idade > 0
    df = df0[df0.age > 0.0]

    #ordenando os dados pela idade
    df2 = df.sort_values(by='age')
    df2 = df2.reset_index()
    del df2['index']

    #dividindo as populacoes
    compr = len(df2)

    pop1 = df2.ix[:(compr/4),:]
    pop2 = df2.ix[(compr/4)+1:(compr/2),:]
    pop3 = df2.ix[(compr/2)+1:(3*(compr/4)),:]
    pop4 = df2.ix[(3*compr/4)+1:compr,:]

    '''
    delta = (df2['age'].max() - df2['age'].min())/4
    pop1 = df2.ix[df2.age < df2['age'].min()+delta]
    pop2 = df2.ix[(df2.age > df2['age'].min()+delta) & (df2.age < df2['age'].min()+2*delta)]
    pop3 = df2.ix[(df2.age > df2['age'].min()+2*delta) & (df2.age < df2['age'].min()+3*delta)]
    pop4 = df2.ix[df2.age > df2['age'].min()+3*delta]
    '''

    #plotando as populacoes
    f, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2, sharex='col', sharey='row')
    plt.axis([-10,80,-10,80])
    ax1.scatter(pop1['x'],pop1['y'], color="blue")
    ax2.scatter(pop2['x'],pop2['y'], color="green")
    ax3.scatter(pop3['x'],pop3['y'], color="goldenrod")
    ax4.scatter(pop4['x'],pop4['y'], color="red")
    plt.savefig('figures/%s/Distribution_4panel_gal_%s.png' %(grupo,galaxies['gal_num'][i_gal]))

    plt.figure()
    plt.axis([-10,80,-10,80])
    plt.scatter(pop1['x'],pop1['y'], color="blue")
    plt.scatter(pop2['x'],pop2['y'], color="green")
    plt.scatter(pop3['x'],pop3['y'], color="goldenrod")
    plt.scatter(pop4['x'],pop4['y'], color="red")
    plt.savefig('figures/%s/Distribution_all_gal_%s.png' %(grupo,galaxies['gal_num'][i_gal]))
    #plt.show()

    '''
    ================================================================================
    Calculando os momentos invariantes de Hu
    ================================================================================

    !======================================================
    !================CENTROIDES DA IMAGEM==================
    !======================================================
    !xc = M10/M00
    !yc = M01/M00
    !
    !onde xc e yc sao os centroides da imagem, M10, M01 e
    !M00 os momentos nao centrais, onde
    !
    !Mpq=Somatorio(x^p.y^q)
    !------------------------------------------------------
    '''

    m10=df2['x'].sum()
    m01=df2['y'].sum()
    cx = int(m10/len(df2))
    cy = int(m01/len(df2))
    re = np.sqrt(len(df2)/3.14)
    tm_total = df2['age'].mean()
    tm_total_std = df2['age'].std()

    print('Centroides (Cx,Cy) da imagem: (%d,%d)' %(cx,cy))
    print('Raio equivalente (m00/pi): %5.3f'%re)

    f = open('data/%s/parametros_hu_%s.txt' %(grupo,galaxies['gal_num'][i_gal]), 'w')
    f.write('#Populacao Rm/re std tm tm_std tp tp_std I1  I2  I3  I4  I5  I6  I7  a   b   f=a+b/2 tetha   Exc     flong   Sim Conc\n')
    f.close()
    arquive = 'data/%s/parametros_hu_%s.txt' %(grupo,galaxies['gal_num'][i_gal])
    obj = str(galaxies['gal_num'][i_gal])

    hu.Humoments(obj,arquive,pop1,re,cx,cy,tm_total,tm_total_std,p=1)
    hu.Humoments(obj,arquive,pop2,re,cx,cy,tm_total,tm_total_std,p=2)
    hu.Humoments(obj,arquive,pop3,re,cx,cy,tm_total,tm_total_std,p=3)
    hu.Humoments(obj,arquive,pop4,re,cx,cy,tm_total,tm_total_std,p=4)

    print('OBJETO #: %s' %i_gal)


fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
