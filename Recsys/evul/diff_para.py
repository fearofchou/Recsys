import numpy as np


fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
with open(fp+'rel_target_log2p1_11.test') as f:
    true = np.array(f.readlines()).astype(float)
import glob

fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/diff_k/'

fl = sorted(glob.glob(fp+'*.pred'))
re = {}
for fn in fl:
    ite = fn.split('/')[-1].split('_')[7]
    dim = fn.split('/')[-1].split('_')[5].split(',')[-1]

    with open(fn) as f:
        pred = np.array(f.readlines()).astype(float)

    try:
        re[int(ite)][int(dim)] = np.sqrt( ((pred-true)**2).mean()  )
    except:
        re[int(ite)] = {}
        re[int(ite)][int(dim)] = np.sqrt( ((pred-true)**2).mean()  )

f = open(fp+'RMSE_diff_k.csv','w')
for ite in sorted(re.keys()):
    f.write('%d,'%(ite))
    for dim in sorted(re[ite].keys()):
        f.write('%.4f,'%(re[ite][dim]))
    f.write('\n')
f.close()

