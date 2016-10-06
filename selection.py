import pandas as pd
import numpy as np
import time
import sql as sql
from sys import exit
from astropy import units as u
from astropy.coordinates import SkyCoord


ini=time.time()

#dfs = pd.read_table('califa_objs.txt', delim_whitespace = True)
#dfs.columns = ['name', 'id', 'ra', 'dec', 'v500','v1200', 'comb', 'ned', 'link']

#df = dfs.ix[:,('name', 'id', 'ra', 'dec')]

dfs = pd.read_csv('califa_master_list_rgb_2012.txt')
#dfs.columns = ['name', 'id', 'rah','ram','ras', 'decD', 'decM', 'decs', 'v500','v1200', 'comb', 'ned', 'link']

df = dfs.ix[:,('#CALIFA_ID','ned_name','ra','dec','Mr','u-r','objID','fiberMag_r','petroMag_u','petroMag_g','petroMag_r','petroMag_i','petroMag_z','petroRad_r','petroR50_r','petroR90_r','z','re')]

df2 = pd.read_table('Paty_at_flux__yx/mapas.txt', delim_whitespace = True)
df2.columns = ['at-flux', 'gal_num']

n=0

for i in range(len(df2)):
    for j in range(len(df)):
        if df2['gal_num'][i]==df['#CALIFA_ID'][j]:
            n=n+1
            df2['ned_name'] = df['ned_name']
            df2['u-r'] = df['u-r']
            df2['re'] = df['re']
            print(n)


df2.to_csv('califa_gal_properts.csv')

df3 = df2.ix[df2['u-r'] < 2.22]
df4 = df2.ix[df2['u-r'] > 2.22]

df3.to_csv('califa_gal_properts_late.csv')
df4.to_csv('califa_gal_properts_early.csv')



fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
