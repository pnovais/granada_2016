import numpy
import math
import pandas as pd

def Humoments(arquive,pop,re,cx,cy,p):
    pca = pop.copy()
    pca['raio'] = numpy.sqrt((pca['x'] - cx)**2 + (pca['y'] - cy)**2)
    Rm = pca['raio'].mean()
    SigR = pca['raio'].std()
    Rm_re = pca['raio'].mean()/re
    SigR_re = pca['raio'].std()/re
    print('')
    print('/'*70)
    print('Hu moments - Populacao %d' %p)
    print('Raio medio Rm: %5.3f +- %5.3f' %(Rm,SigR))
    print('Raio madio ponderado Rm/Re: %5.3f +- %5.3f' %(Rm_re,SigR_re))

    file = open(arquive, 'a')
    '''
    Momentos da imagem
    Ver: http://pt.wikipedia.org/wiki/Momentos_Invariantes_de_uma_Imagem
    '''
    #nao centrais de 2 ordem
    m11=(pca['x']*pca['y']).sum()
    m20=(pca['x']*pca['x']).sum()
    m02=(pca['y']*pca['y']).sum()

    #centrais de 3 ordem
    mu_11=((pca['x']-cx)*(pca['y']-cy)).sum()
    mu_20=((pca['x']-cx)**2).sum()
    mu_02=((pca['y']-cy)**2).sum()

    mu_12=((pca['x']-cx)*((pca['y']-cy)**2)).sum()
    mu_21=((pca['y']-cx)*((pca['x']-cx)**2)).sum()

    mu_30=((pca['x']-cx)**3).sum()
    mu_03=((pca['y']-cy)**3).sum()

    #centrais de 4 ordem
    mu_40=((pca['x']-cx)**4).sum()
    mu_04=((pca['y']-cy)**4).sum()

    #print('Momentos nao centrais m11, m20, m02: %d, %d, %d' %(m11, m20, m02))
    #print('Momentos centrais mu_11, mu_20, mu_02: %d, %d, %d' %(mu_11, mu_20, mu_02))
    #print('Momentos centrais mu_12, mu_21: %d, %d' %(mu_12, mu_21))

    #Momentos invariantes por escala n_ij
    n11=mu_11/(len(pca)**2)
    n12=mu_12/(len(pca)**2.5)
    n21=mu_21/(len(pca)**2.5)
    n02=mu_02/(len(pca)**2)
    n20=mu_20/(len(pca)**2)
    n30=mu_30/(len(pca)**2.5)
    n03=mu_03/(len(pca)**2.5)

    #Momentos invariantes por translacao, escala e rotacao
    #Invariantes de Hu
    I1 = n02 + n20
    I2 = ((n20-n02)**2) + 4*((n11)**2)
    I3 = (n30 - 3*n12)**2 + (3*n21 - n03)**2
    I4 = (n30 + 3*n12)**2 + (3*n21 + n03)**2
    I5 = (n30 - 3*n12)*(n30 + n12)*(((n30 + n12)**2) - 3*((n21 + n03)**2)) + (3*n21 - n03)*(n12 + n03)*(3*((n30 + n12)**2) - ((n21 + n03)**2))
    I6 = (n20 - n02)*((n30 + n12)**2 - (n21 + n03)**2) + 4*n11*(n30 + n12)*(n21 + n03)
    I7 = (3*n21 - n03)*(n30 + n12)*((n30 + n12)**2 - 3*(n21 + n03)**2) - (n30 - 3*n12)*(n21 + n03)*(3*(n30 + n12)**2 - (n21 + n03)**2)

    print('Hu Moments: %5.2e, %5.2e, %5.2e, %5.2e, %5.2e, %5.2e, %5.2e' %(I1, I2, I3, I4, I5, I6, I7))

    #Parametros da Elipse
    dd = (mu_20 + mu_02)
    ee = (mu_20 - mu_02)*(mu_20 - mu_02) + 4*(mu_11)*(mu_11)
    a = numpy.sqrt((2*(dd + numpy.sqrt(ee)))/len(pca))
    b = numpy.sqrt((2*(dd - numpy.sqrt(ee)))/len(pca))
    print('')
    print('Parametros obtidos')
    print('Semi-eixos da elipse (a,b): %5.3f, %5.3f' %(a,b))

    #Razao dos semi-eixos
    f = (a+b)/2
    print('razao dos eixos (a+b/2): %5.3f' %f)

    #Orientacao da Elipse
    tetha = 0.5*numpy.arctan((2*mu_11)/(mu_20 - mu_02))
    print('Orientacao da elipse, tetha: %5.3f' %tetha)

    #Excentricidade
    exc = 1 - (b/a)
    print('Excentricidade da Elipse, e: %5.3f' %exc)

    #FATOR DE ELONGACAO
    flong = numpy.sqrt((mu_02/mu_20))
    print('Fator de elongacao, flong: %5.3f' %flong)
    '''
    Simetria
    '''
    cte = cy - tetha*cx
    sym1 = pca.ix[pca['y'] >= tetha*pca['x'] + cte]
    sym2 = pca.ix[pca['y'] < tetha*pca['x'] + cte]

    SYM = 1 - (math.fabs(len(sym1) - len(sym2))/(len(sym1) + len(sym2)))
    print('')
    print('Parametro de simetria: %5.4f' %SYM)

    '''
    Gini
    '''

    '''
    Concentracao
    '''
    radius=pca.sort_values('raio')
    r20=radius.iat[int(0.2*len(pca)),-1]
    r80=radius.iat[int(0.8*len(pca)),-1]
    Conc = 0.5*numpy.log((r80/r20))

    arr1=pca['x']
    arr2=pca['y']
    arr=numpy.zeros(shape=len(pca))
    arr3=pd.DataFrame(arr)
    n=len(pca)
    l=1
#    fof = fof_fortran.fof(arr1, arr2,arr3,l,n)
#    df_fof=pd.DataFrame(fof)
#    df_fof.columns = ['fof']
#    print(df_fof.describe())
    file.write('%s %s %s %s %s %s %s %s %s  %s %s %s %s %s %s %s %s %s\n' %(p, Rm_re, SigR_re, I1, I2, I3, I4, I5, I6, I7, a, b, f,
                tetha, exc, flong, SYM, Conc))
    return()
