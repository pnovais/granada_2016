"""
Programa para analise dos mapas de idade do CALIFA, utilizando a pipeline x.x
29/09/16

Versao 0.0

------------------------
Versao 0.1
Com correlacao entre os parametros

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



fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
