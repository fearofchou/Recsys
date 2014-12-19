import numpy as np
import glob

#libfm format to graphchi
data_id = 11
tr_te = ['train','test']
tr_te = tr_te[1]
norm_tar = ['','log2p1_','5I_']
tid = 0
fp = '/home/fearofchou/data/KKBOX/libfm/tr_te_data_BS/split_by_month/long_term_playcount_mean/'
uid_fn = 'rel_uid_%02d.%s'%(data_id,tr_te)
sid_fn = 'rel_sid_%02d.%s'%(data_id,tr_te)

with open(fp+uid_fn) as f:
    uid = np.array(f.readlines()).astype(int)
with open(fp+sid_fn) as f:
    sid = np.array(f.readlines()).astype(int)
uid = uid+1
sid = sid+1
for nt in norm_tar:
    tar_fn = 'rel_target_%s%02d.%s'%(nt,data_id,tr_te)
    with open(fp+tar_fn) as f:
        tar = np.array(f.readlines()).astype(float)

    sfp = '/home/fearofchou/data/KKBOX/mymedialite/'
    sfn = 'rel_%02d_%s%s.uir'%(data_id,nt,tr_te)

    f = open(sfp+sfn,'w')

    for idx,val in enumerate(uid):
        f.write('%d %d %f\n'%(uid[idx],sid[idx],tar[idx]))
    f.close()
