import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import wald
import pylab as pl


def chou_wald(Lam,Mu,x):
    result = [0]
    for i in x[1:]:
        result.append( np.sqrt(Lam/(2*np.pi*i**3)) * np.exp(-Lam*(i-Mu)**2)/(2*Mu**2*i)  )

    return np.array(result)

def plt_wald(Lam,Mu,wd):
    leg_str = 'Lambd=%f Mu=%d'%(Lam,Mu)
    plt.plot(wd,'-',label = leg_str)
    plt.legend(loc=1)
    plt.savefig('wald dis')
'''
Mu = [1,1,1,1]
Lam = [0,0.5,1,2]
x=pl.frange(0,100,1)
plt.clf()
for idx in range(len(Mu)):
    print idx
    #wd = wald(Lam[idx],Mu[idx],x)
    wd = wald.pdf(x,Lam[idx],Mu[idx])
    plt_wald(Lam[idx],Mu[idx],wd)
'''

import glob
fl = glob.glob('/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/short_term_playcount/ID_02*')
with open('/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/short_term_playcount/rel_target_02.test') as f:
    true = np.array(f.readlines()).astype('int')

with open('/home/fearofchou/data/KKBOX/fearure_extraction/song_age/rel_songage_201212201301') as f:
    sa = np.array(f.readlines()).astype('int')
f_sa = sa
for idx,val in enumerate(sa):
    if val>12:
        f_sa[idx]=12
    if val<0:
        f_sa[idx]=0
pred = {}
for fn in fl:
    with open(fn) as f:
        pred[fn.split('/')[-1]] = np.array(f.readlines()).astype('float')
x = pl.frange(0,1.3,0.1)
wald_dis = wald.pdf(x,0,0.5)

f_sa =f_sa+1

for fn in pred.keys():
    wald_pred=(wald_dis[f_sa]*pred[fn] + pred[fn])/2
    print fn
    print np.sqrt( ((true-wald_pred)**2).mean() )


