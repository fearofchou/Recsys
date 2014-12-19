import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.cla()
plt.clf()
markers = []
for m in Line2D.markers:
    try:
        if len(m) == 1 and m != ' ':
            markers.append(m)
    except TypeError:
            pass

import numpy as np
markers = np.array(markers)
no_ma = np.array([2,3,4,8,10,12,13,15,16,17])
markers = np.delete(markers,no_ma)
result = {}
result['Diversity'] = div_N_val
result['Freshness'] = fre_N_val
result['Novelty'] = adv_N_val
result['Popularity'] = pop_N_val

FF_ls = sorted(div_N_val[10].keys())
N_ls = sorted(div_N_val.keys())

F_ls = np.array(FF_ls)
idx = [-1,4,3,0,1,2]
F_ls = F_ls[idx]
Eval_metric = {}
for ed in result.keys():
    Eval_metric[ed] = np.zeros([len(F_ls),len(N_ls)])
    for idx,val in enumerate(F_ls):
        for iidx,vval in enumerate(N_ls):
            Eval_metric[ed][idx,iidx] = result[ed][vval][val]

f,ax = plt.subplots(1,4, figsize=(26,6) )
plt.subplots_adjust(hspace=.1)
test ={}
for ii,ed in enumerate(sorted(result.keys())):
    #plt.cla()
    #plt.clf()
    ma_le = 0
    for idx,val in enumerate(F_ls):
        ma = markers[ma_le] + '-'
        fn = val.split('/')[-1]
        fn = fn.split('_')[9]
        test[idx],=ax[ii].plot(N_ls,Eval_metric[ed][idx,:],ma,label = fn)
        ax[ii].set_ylabel(ed,fontsize=18)
        ax[ii].set_xlabel('Number of recommended song',fontsize=18)
        ma_le +=1
        if ii ==3:
            plt.legend(loc=1,prop = {'size':20})
'''
f.legend((test[0],test[1],test[2],test[3],test[4],test[5])\
         ,('U+S','U+MFCC','U+AW','U+AWA','U+AWG','U+AWM')\
         , loc='upper center',ncol=6)
'''
plt.savefig('2.pdf',dpi=1000,format='pdf')

