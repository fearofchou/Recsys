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
result['Adventurousness'] = adv_N_val
result['Popularity'] = pop_N_val



F_ls = np.array(FF_ls)
idx = [-1,4,3,0,1,2]
F_ls = F_ls[idx]
Eval_metric = {}
for ed in result.keys():
    Eval_metric[ed] = np.zeros([len(F_ls),len(N_ls)])
    for idx,val in enumerate(F_ls):
        for iidx,vval in enumerate(N_ls):
            Eval_metric[ed][idx,iidx] = result[ed][vval][val]


plt.subplots(nrows = 1,ncols = 4,sharex = True, sharey = True)
for ii,ed in enumerate(sorted(result.keys())):
    #plt.cla()
    #plt.clf()
    ma_le = 0
    for idx,val in enumerate(F_ls):
        ma = markers[ma_le] + '-'
        fn = val.split('/')[-1]
        fn = fn.split('_')[9]

        plt.plot(N_ls,Eval_metric[ed][idx,:],ma,label = fn)
        plt.ylabel(ed,fontsize=12)
        plt.xlabel('Number of recommender song',fontsize=15)
        ma_le +=1
    '''
    if 'Pop' in ed:
        plt.legend(loc=1)
    else:
        plt.legend(loc=4)
    a=[0]

    a.extend(N_ls)
    '''
    #plt.xticks(a,a)
plt.savefig('2.pdf',dpi=1000,format='pdf')

