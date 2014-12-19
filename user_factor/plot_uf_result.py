import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt


NDCG = {}
for fn in NDCG_fn.keys():
    NDCG[fn] = {}
    for TS in NDCG_fn[fn].keys():
        NDCG[fn][TS] = np.zeros(28372)
        for i in NDCG_fn[fn][TS].keys():
            NDCG[fn][TS][i] = NDCG_fn[fn][TS][i]

uid_len = np.zeros(28372)
for i in UID_dict.keys():
    uid_len[i] = len(UID_dict[i])

UID_us['songs'] = uid_len

from scipy import stats
for fn in NDCG.keys():
    for TS in NDCG[fn]:
        for US in UID_us.keys():
            #zs_us = stats.zscore( UID_us[US] )
            zs_us = UID_us[US]
            idx = NDCG[fn][TS]>0
            plt.xlabel(US)
            plt.ylabel('NDCG@5')
            plt.title(fn+'-'+TS)
            plt.plot(zs_us[idx],NDCG[fn][TS][idx],'x')
            plt.savefig('/home/fearofchou/code/user_factor/plot/'+fn+'_'+TS+'_'+US+'.jpg')
            plt.clf()



