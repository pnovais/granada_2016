import pandas as pd
import numpy as np
import time

ini=time.time()

def dec_HMS2deg(dec=''):
    DEC, rs, ds = '', 1, 1
    D, M, S = dec.split(':')
    if dec:
        D = float(D)
        M = float(M)
        S = float(S)
        if str(D)[0] == '-':
            ds, D = -1, abs(D)
        deg = D + (M/60) + (S/3600)
        DEC = '{0}'.format(deg*ds)
    return DEC


def ra_HMS2deg(ra=''):
    RA, rs, ds = '', 1, 1
    H, M, S = ra.split(':')
    if ra:
        H = float(H)
        M = float(M)
        S = float(S)
        if str(H)[0] == '-':
            rs, H = -1, abs(H)
        deg = (H*15) + (M/4) + (S/240)
        RA = '{0}'.format(deg*rs)
    return RA







df = pd.read_table('califa_coords.txt', delim_whitespace = True)
df.columns = ['name', 'id', 'ra','dec']

ra2=[]
dec2=[]
for i in range(len(df)):
    dec2.append(dec_HMS2deg(dec=str(df['dec'][i])))
    ra2.append(ra_HMS2deg(ra=str(df['ra'][i])))

df['ra2']= ra2
df['dec2']= dec2

df2 = df.ix[:,('name','ra2','dec2')]
df2.to_csv('teste.txt')
'''
with open('test_Coor.txt','wb') as f:
    formats = ['%d','%d','%d']
    np.savetxt(f, df2, delimiter='\t')
'''

fim = time.time()
time_proc = fim - ini
print('')
print('tempo de processamento: %fs' %time_proc)
