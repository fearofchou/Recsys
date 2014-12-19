import numpy as np


fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/short_term_playcount/'
fea = ['uid','sid','target']
data = {}
for i in fea:
    with open(fp+'rel_%s_10.train'%(i)) as f:
        tr = np.array(f.readlines()).astype(int)
    with open(fp+'rel_%s_10.test'%(i)) as f:
        te = np.array(f.readlines()).astype(int)

    data[i] = np.hstack([tr,te])

print 'Start data splitting'
import random,math
da_le = len(data['sid'])
da_range = np.array(range(da_le))
te_le = math.ceil(da_le*0.2)
da_idx = np.zeros(da_le)

te_rs_idx = np.array(random.sample(range(da_le),int(te_le)))
da_idx[te_rs_idx]=1

te_idx = da_idx==1
tr_idx = da_idx==0

rd_da = {}
rd_da['te'] = {}
rd_da['tr'] = {}
print 'test'
for idx,i in enumerate(da_range):
    try:
        rd_da['te']['%d_%d'%(data['uid'][i],data['sid'][i])].append(data['target'][i])
    except:
        rd_da['te']['%d_%d'%(data['uid'][i],data['sid'][i])] = [data['target'][i]]

'''
print 'traing'
for idx,i in enumerate(da_range[tr_idx]):
    try:
        rd_da['tr']['%.0f_%.0f'%(data['uid'][i],data['sid'][i])].append(data['target'][i])
    except:
        rd_da['tr']['%.0f_%.0f'%(data['uid'][i],data['sid'][i])] = [data['target'][i]]

fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_random/'
for i in fea:
    te_f = open(fp + 'rel_%s_44.test'%(i),'w')
    tr_f = open(fp + 'rel_%s_44.train'%(i),'w')
    for j in data[i][tr_idx]:
        tr_f.write('%d\n'%(j))
    for j in data[i][te_idx]:
        te_f.write('%d\n'%(j))
    te_f.close()
    tr_f.close()

'''
