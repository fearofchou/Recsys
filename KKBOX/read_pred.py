import numpy as np
import glob
data_id = 11
pred_format = 'libfm'
pred_format = 'graphchi'
pred_format = 'libfm'
if pred_format == 'libfm':
    fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
    fn = '*%02d*.pred'%(data_id)
    fl = glob.glob(fp+fn)
    pred_tar={}
    for fn in fl:
        kfn = fn.split('/')[-1]
        with open(fn) as f:
            pred_tar[kfn] = np.array(f.readlines()).astype(float)


else:
    #3 for graphchi
    start = 3
    splitter = ' '
    fp = '/home/fearofchou/data/KKBOX/graphchi/'
    fn = '*%02d*.predict'%(data_id)
    fl = glob.glob(fp+fn)
    pred_tar = {}
    for fn in fl:
        with open(fn) as f:
            pred = f.readlines()
        kfn = fn.split('/')[-1]
        pred = pred[start:]
        pred_tar[kfn] = []
        for i in pred:
            pred_tar[kfn].append(float(i.split(splitter)[-1]))

import sys
sys.path.append('/home/fearofchou/code/Recsys/evul/')
from RMSE import*

fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
fn = '*target*%02d*.test'%(data_id)
fl =glob.glob(fp+fn)
true = {}
for fn in fl:
    k = fn.split('/')[-1].split('_')[2]
    with open(fn) as f:
        true[k] = np.array(f.readlines()).astype(float)

#load NL_idx
fp = '/home/fearofchou/data/KKBOX/stats/'
fn = 'rel_%02d.NLidx.npy'%(data_id)
idx = {}
idx['NL_idx'] = np.load(fp + fn)
fn = 'rel_%02d.HLidx.npy'%(data_id)
idx['HL_idx'] = np.load(fp + fn)
idx['All'] = np.array(range(len(true[k])))

#Compute RMSE
f = open('/home/fearofchou/data/KKBOX/result/KKBOX_RMSE_%02d.csv'%(data_id),'w')
for j in idx.keys():
    NHL = idx[j]
    print j
    for i in sorted(pred_tar.keys()):
        if 'log2p1' == i:
            k='log2p1'
            RMSE_val = RMSE(true[k][NHL],np.array(pred_tar[i])[NHL])
        elif '5Ilog2p1' in i:
            k='5Ilog2p1'
            RMSE_val = RMSE(true[k][NHL],np.array(pred_tar[i])[NHL])
        elif '5I' in i:
            k='5I'
            RMSE_val = RMSE(true[k][NHL],np.array(pred_tar[i])[NHL])
        else:
            k='%02d.test'%(data_id)
            RMSE_val = RMSE(true[k][NHL],np.array(pred_tar[i])[NHL])
        fea = i.split('_')[-1].split('.')[0]
        dim = i.split('_')[6]
        f.write('%s,%s,%s,%s'%(k,dim,j,fea))
        print '%s RMSE=%.4f'%(i,RMSE_val)
        f.write(',%.4f\n'%(RMSE_val))
f.close()
    #RMSE_val = RMSE(true,np.array(pred_tar))
