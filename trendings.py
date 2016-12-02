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


df1 = pd.read_csv('data/2all_parameters_group1.csv')
df2 = pd.read_csv('data/2all_parameters_group2.csv')
df3 = pd.read_csv('data/2all_parameters_group3.csv')

frames = [df1, df2, df3]
df = pd.concat(frames)


'''
CORRELACOES
'''
#Correlacoes > 0.6 para Rmedio
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.scatter(df['Rm/re'], df.I1, c='#41ae76')
ax1.set_ylabel('I1')
ax2.scatter(df['Rm/re'],df.I2, c='#238b45')
ax2.set_ylabel('I2')
ax3.scatter(df['Rm/re'],df.a, c='#005824')
ax3.set_ylabel('a')
ax3.set_xlabel('Raio medio')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('R_correlations')


f, (ax5, ax6, ax7) = plt.subplots(3)
ax5.scatter(df.I1,df.a, c='#005824')
ax5.set_xlabel('I1')
ax5.set_ylabel('a')
ax6.scatter(df.I2,df.b, c='#005824')
ax6.set_xlabel('I2')
ax6.set_ylabel('b')
ax7.scatter(df.I2,df.Exc, c='#005824')
ax7.set_xlabel('I2')
ax7.set_ylabel('Exc')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('outras_corr1')


f, (ax5, ax6, ax7) = plt.subplots(3)
ax5.scatter(df.Exc,df.I3, c='#005824')
ax5.set_ylabel('I3')
ax6.scatter(df.Exc,df.I6, c='#005824')
ax6.set_ylabel('I6')
ax7.scatter(df.Exc,df.b, c='#005824')
ax6.set_ylabel('b')
ax7.set_xlabel('Excent')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('outras_corr2')

f, (ax5, ax6, ax7) = plt.subplots(3, sharex=True)
ax5.scatter(df.Exc,df.I2, c='#005824')
ax5.set_ylabel('I2')
ax6.scatter(df.Exc,df.I3, c='#005824')
ax6.set_ylabel('I3')
ax7.scatter(df.Exc,df.I6, c='#005824')
ax7.set_ylabel('I6')
ax7.set_xlabel('Excentricidade')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('exc_corr')


'''
TRENDINGS
'''
#Trendings > 0.3 para Rmedio
f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.scatter(df['Rm/re'],df.tp, c='#99d8c9')
ax1.set_ylabel('Age Pop.')
ax2.scatter(df['Rm/re'],df.M_p, c='#66c2a4')
ax2.set_ylabel('"Mass" Pop.')
ax3.scatter(df['Rm/re'],df['f=a+b/2'], c='#41ae76')
ax3.set_ylabel('fab')
ax3.set_xlabel('Raio medio')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('R_trendings1')

f, (ax4, ax5) = plt.subplots(2, sharex=True)
ax4.scatter(df['Rm/re'],df['Exc'], c='#238b45')
ax4.set_ylabel('Excent')
ax5.scatter(df['Rm/re'],df['Conc'], c='#005824')
ax5.set_ylabel('Conc')
ax5.set_xlabel('Raio medio')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('R_trendings2')


#Trendings > 0.3 para Massa total
f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
ax1.scatter(df['M_t'],df.I2, c='#99d8c9')
ax1.set_ylabel('I2')
ax2.scatter(df['M_t'],df.I3, c='#66c2a4')
ax2.set_ylabel('I3')
ax3.scatter(df['M_t'],df.I4, c='#41ae76')
ax3.set_ylabel('I4')
ax4.scatter(df['M_t'],df.I6, c='#238b45')
ax4.set_ylabel('I6')
ax4.set_xlabel('Massa total')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('Mt_trendings1')

f, (ax5, ax6, ax7) = plt.subplots(3, sharex=True)
ax5.scatter(df['M_t'],df.b, c='#005824')
ax5.set_ylabel('b')
ax6.scatter(df['M_t'],df['f=a+b/2'], c='#005824')
ax6.set_ylabel('fab')
ax7.scatter(df['M_t'],df.Exc, c='#005824')
ax7.set_ylabel('Exc')
ax7.set_xlabel('Densidade de massa total')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('Mt_trendings21')

f, (ax6, ax7) = plt.subplots(2, sharex=True)
ax6.scatter(df['M_t'],df['tp'], c='#005824')
ax6.set_ylabel('idade media populacao')
ax6.set_xlabel('Densidade de massa total')
ax7.scatter(df['M_p'],df.tm, c='#005824')
ax7.set_ylabel('idade media total')
ax7.set_xlabel('Densidade de massa populacao')
plt.savefig('Mt_corr')


f, (ax5, ax6, ax7) = plt.subplots(3, sharex=True)
ax5.scatter(df['M_p'],df.I1, c='#005824')
ax5.set_ylabel('I1')
ax6.scatter(df['M_p'],df.I2, c='#005824')
ax6.set_ylabel('I2')
ax7.scatter(df['M_p'],df.I3, c='#005824')
ax7.set_ylabel('I3')
ax7.set_xlabel('Densidade de massa pop.')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('Mp_trendings1')

f, (ax6, ax7) = plt.subplots(2, sharex=True)

ax6.scatter(df['M_p'],df.I4, c='#005824')
ax6.set_ylabel('I4')
ax7.scatter(df['M_p'],df.Conc, c='#005824')
ax7.set_ylabel('Concent.')
ax7.set_xlabel('Densidade de massa pop.')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('Mp_trendings2')


f, (ax5, ax6, ax7) = plt.subplots(3)
ax5.scatter(df.Exc,df.I1, c='#005824')
ax5.set_xlabel('Exc')
ax5.set_ylabel('I1')
ax6.scatter(df.a,df.I2, c='#005824')
ax6.set_ylabel('I2')
ax6.set_xlabel('a')
ax7.scatter(df.Sim,df.I4, c='#005824')
ax7.set_ylabel('I4')
ax7.set_xlabel('Simetria')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('outros_trendings1')



f, (ax5, ax6, ax7) = plt.subplots(3)
ax5.scatter(df.b,df.I4, c='#005824')
ax5.set_ylabel('I4')
ax6.scatter(df.b,df.I6, c='#005824')
ax6.set_ylabel('I6')
ax7.scatter(df.b,df.I5, c='#005824')
ax7.set_ylabel('I5')
ax7.set_xlabel('b')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('outros_trendings2')


#Excentricidade
f, (ax5, ax6, ax7) = plt.subplots(3, sharex=True)
ax5.scatter(df.Exc,df['Rm/re'], c='#005824')
ax5.set_ylabel('Raio medio')
ax6.scatter(df.Exc,df.M_t, c='#005824')
ax6.set_ylabel('Dens. massa total')
ax7.scatter(df.Exc,df.Conc, c='#005824')
ax7.set_ylabel('Concentracao')
ax7.set_xlabel('Excentricidade')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('exc_trendings1')

f, (ax5, ax6, ax7) = plt.subplots(3, sharex=True)
ax5.scatter(df.Exc,df.I1, c='#005824')
ax5.set_ylabel('I1')
ax6.scatter(df.Exc,df.I4, c='#005824')
ax6.set_ylabel('I4')
ax7.scatter(df.Exc,df.I5, c='#005824')
ax7.set_ylabel('I5')
ax7.set_xlabel('Excentricidade')
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('exc_trendings2')
